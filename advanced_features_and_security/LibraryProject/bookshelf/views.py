from django.shortcuts import render

# Create your views here.
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
