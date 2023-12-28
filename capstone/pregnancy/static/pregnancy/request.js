document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#compose').addEventListener('click', diet_request);
    // Send email when compose form submitted
    document.querySelector('#compose-form').onsubmit = send_request;

    // By default, load the inbox
    load_mailbox('inbox');
  });
