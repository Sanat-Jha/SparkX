from django.shortcuts import render, redirect
from django.contrib.auth.models import User as Auth_User
from django.contrib.auth import authenticate, login
from .models import User, Post
# Create your views here.


# main page where user will scroll posts
def home(request):
    if request.user.is_authenticated:

        user = User.objects.get(Username=request.user.username)
        Posts_ids = user.Postlist
        All_Posts = []

        for post in Posts_ids:
            All_Posts.append( Post.objects.get( Id = post ) )

        context = {
            "user": user,
            "Posts": All_Posts
        }

        return render(request, "home.html", context)

    else:
        return redirect(loginUser)


# Login Page
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


# Sign up page
def sign_up(request):
    if request.method == "POST":
        fname = request. POST. get("first name")
        sname = request. POST. get("second name")
        username = request. POST. get("username")
        email = request. POST. get("email")
        password = request. POST. get("password")

        auth_user = Auth_User.objects.create_user(username,email,password)
        auth_user.save()

        user = User(
            First_name=fname,
            Second_name=sname,
            Username=username,
            Email=email
        )
        user.save()

        return redirect(loginUser)

    return render(request, "sign up.html")


# New post page
def newpost(request):
    if request.method == "POST":
        image = request   .FILES     ["image"]
        caption = request .POST  .get("caption")

        post = Post(
            Image    =  image,
            Caption  =  caption,
            Owner    =  request.user.username
            )
        post.save()

        user = User.objects.get( Username = request.user.username )
        Followers = user.Followers

        for follower in Followers :
            temp_user = User  .objects  .get( Id = follower )
            post_list = temp_user.Postlist
            post_list.append(post.Id)
            temp_user.save()

        return redirect("/")

    return render(request, "newpost.html")




# Notifications page
def notifications(request) :
    return render( request, "notification.html" )




# search page
def search(request) :
    Search     =  request   .POST.get("search")
    keywords   =  Search    .split()
    people     =  User      .objects.all()
    main       =  []

    try :
        main.append( User.objects.get( Username = Search ) )
    
    except :
        pass

    for word in keywords :

        for person in people :
            if word in person.First_name :
                main.append( person )

        for person in people :
            if word in person.Second_name :
                main.append( person )

        for person in people :
            if word in person.Username :
                main.append( person )
