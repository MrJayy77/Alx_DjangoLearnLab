from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# List all books (GET request)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# ViewSet to handle all CRUD operations (Create, Read, Update, Delete)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
