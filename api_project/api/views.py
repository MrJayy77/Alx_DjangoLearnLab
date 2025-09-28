from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# List all books (GET request)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
