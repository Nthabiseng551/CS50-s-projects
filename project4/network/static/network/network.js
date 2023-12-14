function liking(id){
    const likeBtn = event.target;
    const likes = likeBtn.parentElement.querySelector('#like-count');
    let likecount = parseInt(likes.innerText);

    if (likeBtn.className === "btn btn-dark"){
       fetch(`/like/${id}`)
       .then(response => response.json)
       .then(result => {
           likeBtn.className = "btn btn-danger";
           likecount++;
           likes.innerText = likecount;
    })
   }
   else {
       fetch(`/like/${id}`)
       .then(response => response.json)
       .then(result => {
           likeBtn.className = "btn btn-dark";
           likecount--;
           likes.innerText = likecount;
    })
   }
}

function unliking(id){
    const likeBtn = event.target;
    const likes = likeBtn.parentElement.querySelector('#like-count');
    let likecount = parseInt(likes.innerText);

    if (likeBtn.className === "btn btn-danger"){
       fetch(`/like/${id}`)
       .then(response => response.json)
       .then(result => {
           likeBtn.className = "btn btn-dark";
           likecount--;
           likes.innerText = likecount;
    })
   }

}


function editing(id){
const editBtn = event.target;
const originalPost = editBtn.parentElement.querySelector('#post-content').innerText;

if (editBtn.parentElement.querySelector('#edit-btn').innerText === 'Edit'){
   editBtn.parentElement.querySelector('#post-content').innerHTML = `<textarea id="edit-content" rows="5" cols="100"></textarea>`;
   editBtn.parentElement.querySelector('#edit-content').innerText = originalPost;
   editBtn.parentElement.querySelector('#edit-btn').innerText = "Save";
}
else if (editBtn.parentElement.querySelector('#edit-btn').innerText === 'Save'){
   const post = editBtn.parentElement.querySelector('#edit-content').value;
   fetch(`/edit/${id}`, {
       method: 'POST',
       body: JSON.stringify({
           post: post
       })
   })
   .then(response => response.json())
   .then(result => {
       editBtn.parentElement.querySelector('#post-content').innerHTML = result.editted_post;
       editBtn.parentElement.querySelector('#edit-btn').innerHTML = "Edit";
   });
}
}
