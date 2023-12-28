document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#drequest').addEventListener('click', diet_request);
    // Send email when compose form submitted
    document.querySelector('#diet-form').onsubmit = send_request;

  });

function diet_request() {

    // Show compose view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
    document.querySelector('#email-content').style.display = 'none';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
  }
