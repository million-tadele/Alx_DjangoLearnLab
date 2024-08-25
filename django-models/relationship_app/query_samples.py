Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from relationship_app.models import Author, Book, Library, Librarian
... 
... # Query all books by a specific author
... def get_books_by_author(author_name):
...     author = Author.objects.get(name=author_name)
...     books = Book.objects.filter(author=author)
...     return books
... 
... # List all books in a library
... def get_books_in_library(library_name):
...     library = Library.objects.get(name=library_name)
...     books = library.books.all()
...     return books
... 
... # Retrieve the librarian for a library
... def get_librarian_for_library(library_name):
...     library = Library.objects.get(name=library_name)
...     librarian = Librarian.objects.get(library=library)
...     return librarian
... 
... # Example usage:
... if __name__ == "__main__":
...     print("Books by George Orwell:", get_books_by_author("George Orwell"))
...     print("Books in Central Library:", get_books_in_library("Central Library"))
...     print("Librarian of Central Library:", get_librarian_for_library("Central Library"))
