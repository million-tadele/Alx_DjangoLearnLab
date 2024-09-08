Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from django.urls import path
... from .views import BookList
... 
... urlpatterns = [
...     path('books/', BookList.as_view(), name='book-list'),
... ]

# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)

# Include the router-generated URL patterns in the URL configuration
urlpatterns = [
    path('', include(router.urls)),
]
