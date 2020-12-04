from django.shortcuts import render, redirect
from django.contrib.auth.models import User as DUser
from django.contrib.auth import authenticate,login
from .models import User, Post
import datetime
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        user = User.objects.get(Username=request.user.username)
        All_Posts = Post.objects.all().order_by("date")
        Posts = []
        Followings = user.Following
        for post in All_Posts:
            temp_user = User.objects.get(Username=post.Owner)
            Id = temp_user.Id
            if str(Id) in Followings:
                Posts.append(post)
        context = {
        "user" : user,
        "Posts" : Posts
        }
        return render(request, "home.html",context)
    else:
        return redirect(loginUser)


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


def newpost(request):
    if request.method == "POST":
        image = request.POST.get("image")
        caption = request.POST.get("caption")
        post = Post(Image=image,Caption=caption,date=datetime.datetime.now())
        post.save()
    return render(request,"newpost.html")