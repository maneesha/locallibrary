from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.

# admin.site.register(Book)
# Instead of simple admin.site.register we can crate class to register AuthorAdmin. This allows customization of admin panel.
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)
# admin.site.register(Language)


class AuthorAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Author, AuthorAdmin)


@admin.register(Book)  # This decorator does exactly the same thing as the admin.site.register() syntax
class BookAdmin(admin.ModelAdmin):
    pass 


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass 