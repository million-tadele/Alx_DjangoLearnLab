Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # api/urls.py
... from django.urls import path
... from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
... 
... urlpatterns = [
...     path('books/', BookListView.as_view(), name='book-list'),
...     path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
...     path('books/create/', BookCreateView.as_view(), name='book-create'),
...     path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
...     path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
... ]
