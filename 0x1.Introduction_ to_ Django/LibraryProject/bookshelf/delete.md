### Delete the Book Instance
"from bookshelf.models import Book"
```python
book.delete()
books = Book.objects.all()
print(books)

