document.addEventListener('DOMContentLoaded', function() {
  const editBtn = document.querySelector('#edit-btn');
  editBtn.addEventListener('click', function() {
      const originalPost = document.querySelector('#post-content').innerText;
      const id = document.querySelector('#postdiv').dataset.id;

      if (editBtn.innerHTML === 'Edit'){
          document.querySelector('#post-content').innerHTML = `<textarea id="edit-content" rows="5" cols="100"></textarea>`;
          document.querySelector('#edit-content').innerText = originalPost;
          editBtn.innerHTML = "Save";
      }
      else if (editBtn.innerHTML === 'Save'){
          const post = document.querySelector('#edit-content').value;
          fetch(`/edit/${id}`, {
              method: 'POST',
              body: JSON.stringify({
                  post: post
              })
          })
          .then(response => response.json())
          .then(result => {
              document.querySelector('#post-content').innerHTML = result.editted_post;
              editBtn.innerHTML = "Edit";
          });
      }
  })

})




