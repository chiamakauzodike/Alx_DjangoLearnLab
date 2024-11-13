from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author 
 
def get_books_by_author(author_name): 
    try: 
        #author_name = "George Orwell"
        author = Author.objects.get(name=author_name) 
        books = author.books.all() 
        books_by_author = Book.objects.filter(author=author)
        for book in books_by_author:
            print(book.title)
        return books_by_author 
    except Author.DoesNotExist: 
        return f"Author '{author_name}' does not exist." 
    
    # Query 2: List all books in a library 
    
def get_books_in_library(library_name): 
    try:
        library = Library.objects.get(name=library_name) 
        books = library.books.all() 
        return books 
    except Library.DoesNotExist: 
        return f"Library '{library_name}' does not exist." 
        
        # Query 3: Retrieve the librarian for a library 
        
def get_librarian_for_library(library_name): 
    try: 
        library = Library.objects.get(name=library_name) 
        librarian = library.librarian 
        return librarian 
    except Library.DoesNotExist: 
        return f"Library '{library_name}' does not exist." 
    except Librarian.DoesNotExist: 
        return f"There is no librarian assigned to the library '{library_name}'."