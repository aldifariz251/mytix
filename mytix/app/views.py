from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def Index(request):
    return render(request, "index.html")

def Create(request):
    if request.method=="POST":
        username= request.POST["username"]
        email= request.POST["email"]
        password= make_password(request.POST["password"])

        obj = User.objects.create(username=username, email= email, password= password)
        obj.save()
        return redirect('/login')

def RegisterPage(request):
    return render(request, "register.html")

def LoginPage(request):
    return render(request, "login.html")


def ResetPassword(request):
    return render(request, "resetpassword.html")


