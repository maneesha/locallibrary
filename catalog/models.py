from django.db import models
from django.db import reverse # used to generate URLs by reversing the URL patterns 

# Create your models here.

class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        """String for representing the model object"""
        return self.name


