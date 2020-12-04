from django.shortcuts import render, redirect
from django.contrib.auth.models import User as DUser
from django.contrib.auth import authenticate,login
from .models import User, Post

# Create your views here.


def home(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return redirect(loginUser)
    context = {
        "username" : username
    }
    return render(request, "home.html",context)


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "login.html")
    return render(request, "login.html")


def sign_up(request):
    if request.method == "POST":
        fname = request.POST.get("first name")
        sname = request.POST.get("second name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        duser = DUser.objects.create_user(username, email, password)
        duser.save()
        user = User(First_name=fname, Second_name=sname,
                    Username=username, Email=email)
        user.save()

        return redirect(login)
    return render(request, "sign up.html")
