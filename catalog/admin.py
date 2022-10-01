from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.

# admin.site.register(Book)
# Instead of simple admin.site.register we can crate class to register AuthorAdmin. This allows customization of admin panel.
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)
# admin.site.register(Language)


class BooksInline(admin.TabularInline):
    model = Book 
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death') 

    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    fieldsets = (
        ('Name', {'fields' : ('first_name', 'last_name')}),
        ('Details', {'fields' : [('date_of_birth', 'date_of_death')]})
    )

    inlines = [BooksInline]

admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    # Without the extra = 0 this gives you a bunch of empty instances to use which looks messy
    extra = 0





@admin.register(Book)  # This decorator does exactly the same thing as the admin.site.register() syntax
class BookAdmin(admin.ModelAdmin):
    # genre can't be called directly b/c MtM field can get too big
    # new function defined in models.py Book model
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'book', 'status')

    list_filter = ('status', 'due_back')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass 