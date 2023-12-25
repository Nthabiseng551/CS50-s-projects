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
@csrf_exempt
def index(request):

    if request.method == "POST":
        currentUser = User.objects.get(pk=request.user.id)
        userProfile = UserProfile.objects.get(user=currentUser)
        week = request.POST["week"]
        userProfile.week_of_pregnancy = week
        userProfile.pregnant = True
        userProfile.save()

        messages.success(request, 'Week of pregnancy successfully updated')
        return HttpResponseRedirect(reverse("index"))
    else:
        if request.user.is_authenticated:
            currentUser = User.objects.get(pk=request.user.id)
            userProfile = UserProfile.objects.get(user=currentUser)
            week = userProfile.week_of_pregnancy
            to_go = 40 - week
            preg = userProfile.pregnant
            return render(request, "pregnancy/index.html",{
                "week": week,
                "togo": to_go,
                "pregnant": preg
            })
        else:
            return render(request, "pregnancy/index.html")

@csrf_exempt
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

@csrf_exempt
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@csrf_exempt
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
            newProfile = UserProfile(
            user = user,
            pregnant = False,
            dietician = False,
            counsellor = False,
            week_of_pregnancy = 0
            )
            newProfile.save()
        except IntegrityError:
            return render(request, "pregnancy/register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "pregnancy/register.html")

def professionals(request):
    return render(request, "pregnancy/professionals.html")

# Function for users to sign up as dieticians
@csrf_exempt
def dietician(request):
    if request.method == "POST":
        username = request.POST["username"]
        currentUser = request.user

        if username != currentUser.username:
            return render(request, "pregnancy/dietician.html", {
                "message": "Please provide your valid username."
            })
        userProfile = UserProfile.objects.get(user=currentUser)
        if userProfile.dietician:
             return render(request, "pregnancy/dietician.html", {
                "message": "You are already registered as dietician."
            })
        userProfile.dietician = True
        userProfile.save()

        messages.success(request, 'Dietician sign up form successfully submitted')
        return HttpResponseRedirect(reverse("professionals"))
    else:
        return render(request, "pregnancy/dietician.html")

# Function for users to sign up as counsellors
@csrf_exempt
def counsellor(request):
    if request.method == "POST":
        username = request.POST["username"]
        currentUser = request.user

        if username != currentUser.username:
            return render(request, "pregnancy/counsellor.html", {
                "message": "Please provide your valid username."
            })
        userProfile = UserProfile.objects.get(user=currentUser)
        if userProfile.counsellor:
             return render(request, "pregnancy/counsellor.html", {
                "message": "You are already registered as counsellor."
            })
        userProfile.counsellor = True
        userProfile.save()
        messages.success(request, 'Prenatal counsellor sign up form successfully submitted')

        return HttpResponseRedirect(reverse("professionals"))
    else:
        return render(request, "pregnancy/counsellor.html")

def health(request):
    return render(request, "pregnancy/health.html")

def weight(request):
    currentUser = User.objects.get(pk=request.user.id)
    userProfile = UserProfile.objects.get(user=currentUser)

    if request.method == "POST":
        current_weight = request.POST["cweight"]
        if not request.POST["pre-weight"]:
            preWeight = userProfile.pre_weight
        else:
            preWeight = request.POST["pre-weight"]

        if not request.POST["tweight"]:
            tWeight = userProfile.target_weight
        else:
            tWeight = request.POST["tweight"]

        return
    else:
        preWeight = userProfile.pre_weight
        tWeight = userProfile.target_weight
        cWeight = userProfile.current_weight
        
        return render(request, "pregnancy/weight.html")
