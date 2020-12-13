from django.shortcuts import render, redirect
from django.contrib.auth.models import User as DUser
from django.contrib.auth import authenticate,login
from .models import User, Post
from .forms import *
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        user = User.objects.get(Username=request.user.username)
        Posts_ids = user.Postlist
        All_Posts = []
        for post in Posts_ids:
            All_Posts.append(Post.objects.get(Id = post))
        context = {
        "user" : user,
        "Posts" : All_Posts
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

        return redirect(loginUser)
    return render(request, "sign up.html")


def newpost(request):
    if request.method == "POST":
        image = request.FILES["image"]
        caption = request.POST.get("caption")
        print()
        post = Post(Image=image,Caption=caption,Owner=request.user.username)
        post.save()
        user = User.objects.get(Username=request.user.username)
        Followers = user.Followers
        for follower in Followers:
            temp_user = User.objects.get(Id=follower)
            post_list = temp_user.Postlist
            post_list.append(post.Id)
            temp_user.save()
        return redirect("/")
    form = POST() 
    return render(request,"newpost.html", {'form' : form})

def notifications(request):
    return render(request,"notification.html")