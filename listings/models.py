from django.db import models

# Create your models here.
class Listing(models.Model): #inheritance -> class interpreted as a DB table
    # add columns in a table
    title = models.CharField(max_length=150)
    price = models.IntegerField() #or Decimal/Float field
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    # image -> more complicated


