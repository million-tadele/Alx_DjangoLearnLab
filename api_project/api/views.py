from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# api/views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard CRUD operations for the Book model.
    """
    queryset = Book.objects.all()  # All books from the database
    serializer_class = BookSerializer  # The serializer to convert between model and JSON
