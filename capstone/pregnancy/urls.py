from django.urls import path
from . import views

urlpatterns = [
     path("", views.index, name="index"),
     path("login", views.login_view, name="login"),
     path("logout", views.logout_view, name="logout"),
     path("register", views.register, name="register"),
     path("professionals", views.professionals, name="professionals"),
     path("counsellor", views.counsellor, name="counsellor"),
     path("dietician", views.dietician, name="dietician"),
     path("health", views.health, name="health"),
     path("weight", views.weight, name="weight"),
     path("tests", views.tests, name="tests"),
     path("requests/", views.counsellor_request, name="counsellor_request"),
     path("request/", views.diet_request, name="diet_request")
 ]
