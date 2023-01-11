from django.db import models

# Create your models here.

# WARNING: EVERY TIME YOU ADD A FIELD YOU NEED TO RUN: python manage.py makemigrations +  python manage.py migrate!!!

class Listing(models.Model): #inheritance -> class interpreted as a DB table
    # add columns in a table
    title = models.CharField(max_length=150)
    price = models.IntegerField() #or Decimal/Float field
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField() #storing only the link to the file! not the actual file -> Pillow


    def __str__(self):
        # Rename object from Listing object (1) to the title (in the app)
        return self.title


