from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

import json
from datetime import datetime
from .models import User, Post, UserFollowing, PostLike
from django.core.paginator import Paginator


def index(request):
    posts = Post.objects.all().order_by("timestamp").reverse()
    # Paginator (10 posts per page)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_posts = paginator.get_page(page_number)

    likes = PostLike.objects.all()
    liked = []
    #check if current user liked a post
    for like in likes:
            if like.user.id == request.user.id:
                liked.append(like.post.id)
                break
            else:
                liked = []

    # number of likes for each post
    for post in posts:
        num_likes = PostLike.objects.filter(post=post).count()

    return render(request, "network/index.html", {
        "page_posts": page_posts,
        "liked": liked,
        "num_likes": num_likes
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def new_post(request):
    if request.method == "POST":
        # current user
        user = request.user

        # Get post's content
        post = request.POST["post"]
        newpost = Post(
            post = post,
            timestamp = datetime.now(),
            post_by = user
        )
        newpost.save()
        # Redirect user to index
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/newpost.html")

def profile(request, user_id):
    userProfile = User.objects.get(pk=user_id)
    currentUser = User.objects.get(pk=request.user.id)
    username = userProfile.username
    posts = Post.objects.filter(post_by=userProfile).order_by("timestamp").reverse()
    # Paginator (10 posts per page)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_posts = paginator.get_page(page_number)

    # Following and followers
    following = userProfile.follower.all()
    followers = userProfile.following.all()

    #check if current user is a follower
    try:
        userFollow = followers.filter(following_user=currentUser)
        if len(userFollow) == 0:
            isFollower = False
        else:
            isFollower = True
    except:
        isFollower = False

    return render(request, "network/profile.html", {
        "page_posts": page_posts,
        "username": username,
        "following": len(following),
        "followers": len(followers),
        "isFollower": isFollower,
        "userProfile": userProfile,
        "currentUser": currentUser
    })

@csrf_exempt
def follow(request, user_id):
    userProfile = User.objects.get(pk=user_id)
    user_id = userProfile.id
    currentUser = User.objects.get(pk=request.user.id)

    follow = UserFollowing(
        user = userProfile,
        following_user = currentUser
    )
    follow.save()
    return HttpResponseRedirect(reverse("profile", args=(user_id, )))

@csrf_exempt
def unfollow(request, user_id):
    userProfile = User.objects.get(pk=user_id)
    user_id = userProfile.id
    currentUser = User.objects.get(pk=request.user.id)

    follow = UserFollowing.objects.get(
        user = userProfile,
        following_user = currentUser
    )
    follow.delete()
    return HttpResponseRedirect(reverse("profile", args=(user_id, )))


def following(request):
    #current user
    user = User.objects.get(pk=request.user.id)

    following = user.follower.all()
    posts = Post.objects.all().order_by("timestamp").reverse()

    followingPosts = []

    for post in posts:
        for person in following:
            if person.user == post.post_by:
                followingPosts.append(post)

    # Paginator (10 posts per page)
    paginator = Paginator(followingPosts, 10)
    page_number = request.GET.get("page")
    page_posts = paginator.get_page(page_number)
    return render(request, "network/following.html", {
        "page_posts": page_posts
    })

# API function for editing posts
@csrf_exempt
def edit(request, post_id):
    original_post = Post.objects.get(pk=post_id)

    data = json.loads(request.body)
    editted_post = data.get("post")
    original_post.post = editted_post
    original_post.save()

    return JsonResponse({ "editted_post": editted_post })

# API function for liking posts
@csrf_exempt
def like(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)
    data = json.loads(request.body)
    post_likes = data.get("likes")
    post.likes = post_likes
    post.likes.add(user)
    

    return JsonResponse({ "post_likes": post_likes })

# API function for unlike posts
@csrf_exempt
def unlike(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=request.user.id)

    post.likes.remove(user)
    return JsonResponse({ "post_likes": post_likes })
