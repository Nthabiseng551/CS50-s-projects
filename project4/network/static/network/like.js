document.addEventListener('DOMContentLoaded', function() {
    var likeBtn = document.getElementById('like-btn');

    function liking(){
        if (likeBtn.className === "btn btn-danger"){
            fetch(`/unlike/${post.id}`)
            .then(response => response.json)
            .then(result => {
                console.log(result.num_likes);
                likeBtn.className === "btn btn-dark";
            })
        }
        else if (likeBtn.className === "btn btn-dark"){
            fetch(`/like/${post.id}`)
            .then(response => response.json)
            .then(result => {
                console.log(result.num_likes);
                likeBtn.className === "btn btn-danger";
            })
        }
    }
})



