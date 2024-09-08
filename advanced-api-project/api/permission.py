Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from rest_framework.permissions import IsAuthenticatedOrReadOnly
... 
... class BookListView(generics.ListAPIView):
...     permission_classes = [IsAuthenticatedOrReadOnly]
...     queryset = Book.objects.all()
...     serializer_class = BookSerializer
... 
... class BookCreateView(generics.CreateAPIView):
...     permission_classes = [IsAuthenticatedOrReadOnly]
...     queryset = Book.objects.all()
...     serializer_class = BookSerializer
