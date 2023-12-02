document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // When Compose form is submitted
  document.querySelector('#compose-form').addEventListener('submit', send_email);


  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#emails-content').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function view_email(id){

  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
    // Print email
      console.log(email);
      // Show email content and hide other views
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'none';
      document.querySelector('#emails-content').style.display = 'block';

      document.querySelector('#emails-content').innerHTML = `
          <p>${email.sender}: ${email.subject} : ${email.timestamp} : ${email.recipient}</p>
          <p>${email.body}</p>
      `;
      // read vs unread
      if (!email.read){
        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({
              read: true
          })
        })
      }
      // archived
      const archive = document.createElement('button');
      if (email.archived){
        archive.innerHTML = "Unarchive";
      }
      else{
        archive.innerHTML = "Archive";
      }
      element.addEventListener('click', function() {
        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({
              archived: !email.archived
          })
        })
        .then(() => {
          load_mailbox('inbox')
        })
      });
      document.querySelector('#email-content').append(archive);

      // Reply
      const reply = document.createElement('button');
      reply.innerHTML = "Reply"
      reply.addEventListener('click', function() {
       compose_email();

       let subject = email.subject;
       if(subject.split(' ',1)[0] != "Re:"){
          subject = "Re: " + email.subject;
       }

       document.querySelector('#compose-subject').value = subject;
       document.querySelector('#compose-recipients').value = email.sender;
       document.querySelector('#compose-body').value = `On ${email.timestamp} ${email.sender} wrote: ${email.body}`;
      });
      document.querySelector('#email-content').append(reply);
  });
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-content').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Get list of emails in mailbox
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // Print emails
       console.log(emails);
       emails.forEach(email => {
        const mail = document.createElement('div');
        mail.className = "List-group-item"; //bootstrap component, im going to change component then set background color in css to white(default for unread)
        mail.innerHTML = `
        <p>${email.sender}: ${email.subject} : ${email.timestamp}</p>
        `;
        // Change email background color when the email is read(clicked on) or unread
        mail.addEventListener('click', view_email(email.id));
        document.querySelector('#emails-view').append(mail);
       })
});
}

function send_email() {

  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;

  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
    })
  })
  .then(response => response.json())
  .then(result => {
      // Print result
      console.log(result);
      load_mailbox('sent');
  });
}

