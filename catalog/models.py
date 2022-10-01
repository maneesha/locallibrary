from django.db import models
from django.urls import reverse # used to generate URLs by reversing the URL patterns 
import uuid # Universally Unique Identifier. Required for unique book instances. Used as alternative to AutoField for primary_key?

# Create your models here.

class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        """String for representing the model object"""
        return self.name

class Language(models.Model):
    """Model repesenting book language"""

    # Ideally this would be drop down but I'm leaving it as free text for now
    language = models.CharField(max_length=100, help_text="Enter the language the book is written in")

    def __str__(self):
        """String representation of language"""
        return self.language


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

    language = models.ForeignKey(Language, help_text = "Select the book's language", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """string for representing the model object"""

        return self.title

    def get_absolute_url(self):
        """Returns URL to access detail record for book"""

        return reverse('book-detail', args = [str(self.id)])


class BookInstance(models.Model):
    """Model representing a specific copy of a book"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book")

    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)

    imprint = models.CharField(max_length=200)

    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text="Book Availability"
    )

    class Meta:
        ordering = ['due_back']

    
    def __str__(self):
        """String for representing the Model object"""

        return f'{self.id} ({self.book.title})'

class Author(models.Model):
    """Model representing an author"""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns URL to access a particular author instance"""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """Returns string for representing the Model object"""
        return f'{self.last_name}, {self.first_name}'