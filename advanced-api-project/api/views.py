from django.shortcuts import render

# Create your views here.
# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer



class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'


class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

