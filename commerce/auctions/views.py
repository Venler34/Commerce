from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Bid, Comment, AuctionListing, Category


def index(request):
    return render(request, "auctions/index.html", {
        "AuctionListings" : AuctionListing.objects.all()
    })


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


def createListing(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        startingBid = request.POST["startingBid"]
        category = request.POST["category"]
        imgURL = request.POST["imgURL"]

        errors = []

        if not title:
            errors.append("No title")
        if not description:
            errors.append("No description")
        if not startingBid:
            errors.append("No starting Bid")

        if len(errors) > 0:
            return render(request, "auctions/createListing.html", {
                "Errors" : errors,
                "title" : title,
                "description" : description,
                "startingBid" : startingBid,
                "category" : category,
                "imgURL" : imgURL
            })
        else:
            username = request.POST["user"]
            user = User.objects.get(username=username)
            new_auction = AuctionListing(item_name=title, item_description=description, imageURL=imgURL, user=user)
            starting_bid = Bid(price=int(startingBid), user=user, auction=new_auction)

            # check if category exists
            if category:
                if Category.objects.filter(categoryType=category).exists():
                    new_auction.category = Category.objects.get(categoryType=category)
                else:
                    new_category = Category(categoryType=category)
                    new_category.save()
                    new_auction.category = new_category
            
            new_auction.save()
            starting_bid.save()

            return HttpResponseRedirect(reverse("index"))

    return render(request, "auctions/createListing.html", {
        "title" : "",
        "description" : "",
        "startingBid" : "",
        "category" : "",
        "imgURL" : ""
    })

def viewListing(request, id):
    auction = AuctionListing.objects.get(pk=id)
    current_bids = auction.bids
    largest_bid = current_bids.latest('pk').price

    errorMessage = ""
    
    # happens if trying to get greater bid
    if request.method == "POST":
        username = request.POST["username"]
        user = User.objects.get(username=username)
        possible_bid = float(request.POST["bid"])

        numOfBids = current_bids.count()

        if possible_bid > largest_bid or (numOfBids == 1 and possible_bid == largest_bid):
            next_largest = Bid(price=possible_bid, auction=auction, user=user)
            next_largest.save()
        else:
            errorMessage = "Your bid is not high enough"

    # May remove if found unnecessary later on
    largest_bid = current_bids.latest('pk').price

    return render(request, "auctions/viewListing.html", {
        "listing" : auction,
        "current_bid" : largest_bid,
        "message" : errorMessage
    })

def commentListing(request, id):
    auction = AuctionListing.objects.get(pk=id)
    if request.method == "POST":
        content = request.POST["content"]
        username = request.POST["username"]
        user = User.objects.get(username=username)
        comment = Comment(text=content, auction=auction, user=user)
        comment.save()
    
    return HttpResponseRedirect(reverse("viewListing", args=(id,)))

def addWatchlist(request, id, username):
    auction = AuctionListing.objects.get(pk=id)
    user = User.objects.get(username=username)

    user.watchlist.add(auction)
    auction.potentialBuyers.add(user)

    return HttpResponseRedirect(reverse("viewListing", args=(id,)))

def removeWatchList(request, id, username):
    auction = AuctionListing.objects.get(pk=id)
    user = User.objects.get(username=username)

    user.watchlist.remove(auction)

    return HttpResponseRedirect(reverse("viewListing",args=(id,)))

def closeListing(request, id):
    auction = AuctionListing.objects.get(pk=id)
    auction.openListing = False
    auction.save()

    return HttpResponseRedirect(reverse("viewListing",args=(id,)))

def watchlist(request, username):
    user = User.objects.get(username=username)
    return render(request, "auctions/watchList.html", {
        "watchlist" : user.watchlist.all()
    })

def getCategories(request):
    return render(request, "auctions/categories.html", {
        "categories" : Category.objects.all()
    })

def viewCategory(request, category):
    return render(request, "auctions/viewCategories.html", {
        "category" : Category.objects.get(categoryType=category)
    })