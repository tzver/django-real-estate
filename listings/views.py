from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

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


def listing_retrieve(request, pk):
    # How to fetch specific listing? -> use primary key on the model -> id
    listing = Listing.objects.get(id=pk) #get to get a specific listing
    context = {
        "listing": listing
    }

    return render(request, "listing.html", context)



def listing_create(request):
    form = ListingForm() #create a new ListingForm (empty form) -> only creating, not yet
    if request.method == "POST":
        form = ListingForm(request.POST) #populating the form with request data
        # can displayt the error messages
        print(request.POST)
        if form.is_valid():
            # TODO -> need to create a listing with all the data
            form.save() # -> saving all the data in the DB as a new listing
            return redirect("/listings")

    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)# don't want to continue otherwise will return an empty form submitting! -> have to handle that as well -> GET request; if submit, define the type of request


def listing_update(request, pk): #fetch specific listing -> like we did in detailed view
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing) # instance important for django to know what listing we are updating!

    if request.method == "POST":
        form = ListingForm(request.POST) #populating the form with request data
        # can displayt the error messages
        print(request.POST)
        if form.is_valid():
            form.save() # -> saving all the data in the DB as a new listing
            return redirect("/listings")

    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)# don't want to continue otherwise will return an empty form submitting! -> have to handle that as well -> GET request; if submit, define the type of request

def listing_delete(request, pk): #fetch specific listing -> like we did in detailed view
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/listings")


