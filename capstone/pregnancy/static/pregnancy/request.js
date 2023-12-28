document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#drequest').addEventListener('click', diet_request);
    // Send email when compose form submitted
    document.querySelector('#diet-form').onsubmit = send_request;

  });

function diet_request() {

    document.querySelector('#diet-request-view').style.display = 'block';


  }

function send_request() {
    // Get data from compose form submitted
    const concerns = document.getElementsByName('dconcern').value;


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
