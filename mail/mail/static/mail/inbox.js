document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  // Send email when compose form submitted
  document.querySelector('#compose-form').onsubmit = send_email;

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-content').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function view_email(id) {

  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);
      // Show email content and hide other views
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'none';
      document.querySelector('#email-content').style.display = 'block';

      // Display content of email
      document.querySelector('#email-content').innerHTML = `
      <p><strong>From:</strong> ${email.sender}</p>
      <p><strong>To:</strong> ${email.recipients}</p>
      <p><strong>Subject:</strong> ${email.subject}</p>
      <p><strong>Timestamp:</strong> ${email.timestamp}</p>
      <hr>
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
      // archive vs unarchive
      if (email.user !== email.sender){
        const archive = document.createElement('button');
        if (email.archived){
          archive.className = "btn btn-sm btn-outline-primary";
          archive.innerHTML = 'Unarchive';
        }
        else {
          archive.className = "btn btn-sm btn-outline-primary";
          archive.innerHTML = 'Archive';
       }

        archive.addEventListener('click', function() {
          if (email.archived){
            fetch(`/emails/${email.id}`, {
              method: 'PUT',
              body: JSON.stringify({
                  archived: false
              })
            })
            .then (() => {load_mailbox('inbox')});
         }
          else {
            fetch(`/emails/${email.id}`, {
              method: 'PUT',
              body: JSON.stringify({
                  archived: true
              })
            })
            .then (() => {load_mailbox('inbox')});
          }
        });
        document.querySelector('#email-content').append(archive);
      });
}


function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-content').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  // Get emails for particular mailbox
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // Print emails
      console.log(emails);

    // Create a box(div with border) for each email
    emails.forEach(email => {
      const mail = document.createElement('div');
      // Read vs unread
      if (email.read){
        mail.className = "list-group-item list-group-item-dark";
      }
      else {
        mail.className = "list-group-item";
      }

      mail.innerHTML = `<p><strong>${email.sender}</strong> ${email.subject}<span  style="float : right;" class="text-muted">${email.timestamp}</span></p>`;

      // click to view email
      mail.addEventListener('click', () => view_email(email.id));
      document.querySelector('#emails-view').append(mail);
    })
  });
}

function send_email() {
  // Get data from compose form submitted
  const recipients = document.querySelector('#compose-recipients').value;
  const subject = document.querySelector('#compose-subject').value;
  const body = document.querySelector('#compose-body').value;

  // Send data
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

  return false;
}


