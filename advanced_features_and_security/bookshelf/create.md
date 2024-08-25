Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ### Create a Book Instance
... ```python
... from bookshelf.models import Book
... 
... book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
... print(book)
