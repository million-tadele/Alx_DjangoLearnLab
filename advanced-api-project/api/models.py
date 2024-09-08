from django.db import models

# Create your models here.

# api/models.py
from django.db import models

class Author(models.Model):
    """
    Represents an author who writes books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book with its title, publication year, and associated author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


from rest_framework.filters import SearchFilter

class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books with filtering and search capabilities.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']

