from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required


from .models import User, Listing

CATEGORIES = []

def index(request):
    return render(request, "auctions/index.html")


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

# form for creating a new listing
class NewListingForm(forms.Form):
    title = forms.CharField(label="Title for listing", widget=forms.TextInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    description = forms.CharField(label="Description", widget=forms.TextInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    price = forms.FloatField(label="Price", widget=forms.NumberInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    image = forms.URLField(label="Enter image URL", required=False, widget=forms.URLInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))
    category = forms.CharField(label="Category", required=False, widget=forms.TextInput(attrs={'style': 'width: 300px;', 'class': 'form-control'}))

#add login required decorator later
def create_listing(request):
    if request.method == "POST":
        
    else:
        return render(request, "auctions/create.html",{
            "form": NewListingForm()
        })
