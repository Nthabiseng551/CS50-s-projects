from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from datetime import datetime
from .models import User, Post, UserFollowing
from django.core.paginator import Paginator


def index(request):
    posts = Post.objects.all().order_by("timestamp").reverse()
    # Paginator (10 posts per page)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_posts = paginator.get_page(page_number)
    return render(request, "network/index.html", {
        "page_posts": page_posts
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
    user = User.objects.get(pk=user_id)
    username = user.username
    posts = Post.objects.filter(user=user).order_by("timestamp").reverse()
    # Paginator (10 posts per page)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_posts = paginator.get_page(page_number)

    # Following and followers
    following = user.following.all()
    followers = user.followers.all()

    #check if current user is a follower
    for follower in followers:
            if follower == request.user:
                isFollower = True
                break
            else:
                isFollower = False

    return render(request, "network/profile.html", {
        "page_posts": page_posts,
        "username": username,
        "following": len(following),
        "followers": len(followers),
        "isFollower": isFollower,
        "user": user
    })
def follow(request, user_id):
    userProfile = User.objects.get(pk=user_id)
    userProfile.followers.add(request.user)
    user_id = userProfile.id
    return HttpResponseRedirect(reverse(profile, kwargs=('user_id': user_id)))

def unfollow(request, user_id):
    userProfile = User.objects.get(pk=user_id)
    userProfile.followers.remove(request.user)
    user_id = userProfile.id
    return HttpResponseRedirect(reverse("index"))
