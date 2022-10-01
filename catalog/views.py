from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic 

# Create your views here.

def index(request):
    """View function for home page"""

    # Generate counts of objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # All is implied by default
    num_authors = Author.objects.count()

    # Available books (status == 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    all_genres = Genre.objects.values_list('name', flat=True)

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'all_genres': all_genres,
    }

    # Render the HTML template index.html with data from context
    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

