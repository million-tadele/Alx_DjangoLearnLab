from django.shortcuts import render

# Create your views here.

"book_list", "books"
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book

@permission_required('your_app_name.can_view', raise_exception=True)
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'your_app_name/book_detail.html', {'book': book})

@permission_required('your_app_name.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Code to edit the book
    pass

@permission_required('your_app_name.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Code to delete the book
    pass


<!-- form_example.html -->
<form method="post" action="/submit/">
    {% csrf_token %}
    <!-- form fields here -->
    <button type="submit">Submit</button>
</form>

from django.shortcuts import render
from .models import Book

def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})


from django import forms
from .models import Book

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100)
