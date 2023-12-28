document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#').addEventListener('click', diet_request);
    // Send email when compose form submitted
    document.querySelector('#compose-form').onsubmit = send_request;

  });
