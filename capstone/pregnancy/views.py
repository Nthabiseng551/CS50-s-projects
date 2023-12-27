from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import math

from datetime import datetime, date, timedelta

from .models import User, UserProfile, Test

# Create your views here.

@csrf_exempt
def index(request):

    if request.method == "POST":
        currentUser = User.objects.get(pk=request.user.id)
        userProfile = UserProfile.objects.get(user=currentUser)
        week = request.POST["week"]
        userProfile.week_of_pregnancy = week
        userProfile.pregnant = True
        userProfile.week_update_date = date.today()
        userProfile.save()

        messages.success(request, 'Week of pregnancy successfully updated')
        return HttpResponseRedirect(reverse("index"))
    else:
        if request.user.is_authenticated:
            currentUser = User.objects.get(pk=request.user.id)
            userProfile = UserProfile.objects.get(user=currentUser)
            tests = Test.objects.all()
            for test in tests:
                userProfile.tests.add(test)

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
            tests = Test.objects.all()
            for test in tests:
                newProfile.usertests.add(test)
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
    currentUser = User.objects.get(pk=request.user.id)
    userProfile = UserProfile.objects.get(user=currentUser)
    week = userProfile.week_of_pregnancy
    updated_date = userProfile.week_update_date
    # Added timedelta weeks to manipulate current date for the sake of demonstration of incrementing weeks for future dates
    current_date = date.today() + timedelta(weeks=0)

    time_delta = current_date - updated_date
    deltaa = time_delta.days
    weeks = math.floor(deltaa/7) + week
    userProfile.week_of_pregnancy = weeks
    userProfile.week_update_date = current_date
    userProfile.save()
    week = userProfile.week_of_pregnancy

    return render(request, "pregnancy/health.html",{
        "week": week,
        "timedelta": weeks
    })

# Function for pregnant users to track weight gain
def weight(request):
    currentUser = User.objects.get(pk=request.user.id)
    userProfile = UserProfile.objects.get(user=currentUser)

    if request.method == "POST":
        cWeight = request.POST["cweight"]
        userProfile.current_weight = cWeight
        userProfile.pregnant = True
        userProfile.currentWeight_update_date = date.today()
        userProfile.save()
        if not request.POST["pre-weight"]:
            preWeight = userProfile.pre_weight
        else:
            preWeight = request.POST["pre-weight"]
            userProfile.pre_weight = preWeight
            userProfile.pregnant = True
            userProfile.save()

        if not request.POST["tweight"]:
            tWeight = userProfile.target_weight
        else:
            tWeight = request.POST["tweight"]
            userProfile.target_weight = tWeight
            userProfile.pregnant = True
            userProfile.save()

        return HttpResponseRedirect(reverse("weight"))
    else:
        track_weight = True
        preWeight = userProfile.pre_weight
        tWeight = userProfile.target_weight
        cWeight = userProfile.current_weight
        if preWeight is None or tWeight is None or cWeight is None:
            track_weight = False
        elif preWeight is not None and tWeight is not None and cWeight is not None:
            track_weight = True
            percentage_gain = ((cWeight - preWeight)/ tWeight) * 100
            duration_percent = (userProfile.week_of_pregnancy / 40) * 100
            difference = abs(percentage_gain - duration_percent)
            update_date = userProfile.currentWeight_update_date

            return render(request, "pregnancy/weight.html",{
                "percentage_gain": percentage_gain,
                "track_weight": track_weight,
                "duration_percent": duration_percent,
                "difference": difference,
                "date": update_date
            })
        return render(request, "pregnancy/weight.html")

# prenatal tests view
def tests(request):
    currentUser = User.objects.get(pk=request.user.id)
    userProfile = UserProfile.objects.get(user=currentUser)

    tests = userProfile.tests.all()
    for test in tests:
        if test in userProfile.tests.filter(done=True):
            done = True
        elif test in userProfile.tests.filter(done=False):
            done=False


    tests1 = userProfile.tests.filter(trimester=1)

    tests2 = userProfile.tests.filter(trimester=2)

    tests3 = userProfile.tests.filter(trimester=3)

    return render(request, "pregnancy/tests.html", {
        "tests1": tests1,
        "tests2": tests2,
        "tests3": tests3,
        "done": done
    })
