from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime

from .models import User, UserProfile

# Create your views here.

def index(request):
    currentUser = User.objects.get(pk=request.user.id)
    userProfile = UserProfile.objects.filter(user=currentUser)
    if request.method == "POST":

        week = request.POST["week"]
        userProfile.week_of_pregnancy = week
        userProfile.pregnant = True

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "pregnancy/index.html", {
            "userProfile": userProfile
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
            return render(request, "pregnancy/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "pregnancy/login.html")


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
            return render(request, "pregnancy/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "pregnancy/register.html", {
                "message": "Username already taken."
            })
        newProfile = UserProfile(
            user = user,
            pregnant = False,
            dietician = False,
            counsellor = False,
            week_of_pregnancy = 0
        )
        newProfile.save
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "pregnancy/register.html")
