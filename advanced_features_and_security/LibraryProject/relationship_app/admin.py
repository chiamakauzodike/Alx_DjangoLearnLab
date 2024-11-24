from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display =('id', 'name')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =('id', 'title', 'author')
    search_fields = ('title',)
    list_filter = ('author',)

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display =('id', 'name')
    search_fields = ('name',)
    filter_horizontal = ('books',)

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display =('id', 'name', 'library')
    search_fields = ('name', 'library__name')
