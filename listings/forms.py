from django.forms import ModelForm, Form # form that gets generated from a model -> easy way of building forms. Can also work with Form -> mode manual work
from .models import Listing


class ListingForm(ModelForm):
    class Meta: #required when dealing with a model form -> need to specifiy what model you are workig with
        model = Listing
        fields = ["title", 
                    "price", 
                    "num_bedrooms", 
                    "num_bathrooms", 
                    "square_footage", 
                    "address", "image"]#list of field names you want on the form
        