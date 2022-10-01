from django.db import models
from django.db import reverse # used to generate URLs by reversing the URL patterns 
import uuid # Universally Unique Identifier. Required for unique book instances. Used as alternative to AutoField for primary_key?

# Create your models here.

class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        """String for representing the model object"""
        return self.name


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book"""

    title = models.CharField(max_length=200)

    # Author is foreign key bc book has 1 author but author has many books (as future exercise, try converting to ManytoMany field)
    # Author is string for now, not object bc has not yet been declared in the file
    # If the author is deleted, then value becomes null.  CASCADE would delete book if author deleted; PROTECT or RESTRICT would prevent author delete if a book uses it 
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")

    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text="13 character <a href='#'>ISBN number</a>")


    # Genre is manytomany field bc books have multiple genres, genres have multiple books
    # Genre has been defined above so we can use the object rather than a string

    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    def __str__(self):
        """string for representing the model object"""

        return self.title

    def get_absolute_url(self):
        """Returns URL to access detail record for book"""

        return reverse('book-detail', args = [str(self.id)])


