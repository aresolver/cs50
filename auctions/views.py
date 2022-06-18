from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Article, Category

listings = Article.objects.all()
active_listings = Article.objects.filter(active=True)

def index(request):
   
    return render(request, "auctions/index.html", {
        "listings":active_listings
        }
    )


def categories(request):
    pass

def watchlist(request):
    pass

def create_listing(request):

    if request.user.is_authenticated:
         user = request.user
    else:
        return render(request, "auctions/login.html", {
            "message": "Invalid username and/or password."
        })        

    if request.method == "POST":
        name = request.POST["name"]
        desc = request.POST["description"]
        bid = request.POST["bid"]
        url = request.POST["url_image"]
        price = bid
        active = True
     

        #Check if exist default category
        default =  Category.objects.filter(name="None")
        if len(default) == 0:
            c = Category(name="None")
            c.save()
        else:
            c = default.first()

        f = Article(name=name, description=desc, starting_bid=bid,
                    url_image=url, current_price=price, active=active,
                    category=c, user=user)
        # Check if creation successful
        if not f.save():
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create_listing.html", {
                "message": "Error creating list. Try again."
            })            
  
    else:
        return render(request, "auctions/create_listing.html")    


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
