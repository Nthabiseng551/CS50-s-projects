document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#drequest').addEventListener('click', diet_request);
    // Send email when compose form submitted
    document.querySelector('#diet-form').onsubmit = send_request;

  });
