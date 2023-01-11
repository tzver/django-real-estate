from django.shortcuts import render
from .models import Listing

# Create your views here.

# CRUD - create, retrieve (one record), update, delete, list (list multiple records)

# can work with functions or classes
def listing_list(request): # name: model + convention; request is coming from a browser of a user
    # Listings has objects property (all models have it) -> to perform diff operations on a DB

    # fetch all listings in the DB
    listings = Listing.objects.all() #fetches all of the listings from a DB
    context = {
        "listings": listings
    }

    return render(request, "listings.html", context) # return responses -> by returning a Render which takes in a request; template we want to return: "listings.html"context: data you wanna inject in the template
    # add template url to settings.py