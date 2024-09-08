Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# api/test_views.py
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create an author and some books for testing
        self.author = Author.objects.create(name="Author 1")
        self.book1 = Book.objects.create(title="Book 1", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book 2", publication_year=2021, author=self.author)

        # Get the URL for the list view and detail view
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book1.id})
def test_create_book(self):
    url = reverse('book-list')
    data = {
        'title': 'New Book',
        'publication_year': 2022,
        'author': self.author.id
    }
    response = self.client.post(url, data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 3)  # Including the books created in setUp
    self.assertEqual(Book.objects.last().title, 'New Book')
def test_retrieve_book(self):
    response = self.client.get(self.book_detail_url)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], self.book1.title)
def test_update_book(self):
    data = {
        'title': 'Updated Book',
        'publication_year': 2020,
        'author': self.author.id
...     }
...     response = self.client.put(self.book_detail_url, data, format='json')
...     self.assertEqual(response.status_code, status.HTTP_200_OK)
...     self.book1.refresh_from_db()
...     self.assertEqual(self.book1.title, 'Updated Book')
... def test_delete_book(self):
...     response = self.client.delete(self.book_detail_url)
...     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
...     self.assertEqual(Book.objects.count(), 1)
... def test_filter_books_by_title(self):
...     url = f"{self.book_list_url}?title=Book 1"
...     response = self.client.get(url)
...     self.assertEqual(response.status_code, status.HTTP_200_OK)
...     self.assertEqual(len(response.data), 1)
...     self.assertEqual(response.data[0]['title'], 'Book 1')
... def test_search_books_by_author_name(self):
...     url = f"{self.book_list_url}?search=Author 1"
...     response = self.client.get(url)
...     self.assertEqual(response.status_code, status.HTTP_200_OK)
...  def test_order_books_by_publication_year(self):
...     url = f"{self.book_list_url}?ordering=publication_year"
...     response = self.client.get(url)
...     self.assertEqual(response.status_code, status.HTTP_200_OK)
...     self.assertEqual(response.data[0]['publication_year'], 2020)
...    self.assertEqual(len(response.data), 2)
... def test_create_book_requires_authentication(self):
...     self.client.logout()  # Ensure the client is not authenticated
...     data = {
...         'title': 'Unauthenticated Book',
...         'publication_year': 2022,
...         'author': self.author.id
...     }
...     response = self.client.post(self.book_list_url, data, format='json')
...     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
... def test_create_book(self):
...     """
...     Test that a book can be successfully created and stored in the database.
...     """
...     ...
["self.client.login"
