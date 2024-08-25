Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from django.urls import path
... from .views import list_books, LibraryDetailView
... 
... urlpatterns = [
...     path('books/', list_books, name='list_books'),
...     path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
... ]
