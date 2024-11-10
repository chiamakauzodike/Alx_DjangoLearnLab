from relationship_app.models import Author, Book, Library, Librarian

def get_book_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        return books
    except Author.DoesNotExist:
        return f"Author '{author_name}' does not exist."
    
def get_books_in_library(library_name):
    try:
        library = library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return f"Library '{library_name}' does not exist."
    
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return f"There is no librarian assigned to the libary '{library_name}'."