document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#drequest').addEventListener('click', diet_request);
    // Send email when compose form submitted
    document.querySelector('#diet-form').onsubmit = send_request;

  });

function diet_request() {

    document.querySelector('#diet-request-view').style.display = 'block';

    // Clear out composition fields
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
  }
