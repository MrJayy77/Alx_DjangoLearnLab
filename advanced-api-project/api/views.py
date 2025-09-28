from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# List all books — available to everyone (Read-Only)
class BookListView(generics.ListAPIView):
    """
    GET /books/
    Returns a list of all books in the database.
    This view is open to all users (no authentication required).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can view books


# Retrieve a single book by ID — available to everyone
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Retrieves details of a single book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book — only for authenticated users
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Allows authenticated users to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users can create

    # Optional customization — automatically validate or modify data before saving
    def perform_create(self, serializer):
        """
        Custom behavior to execute after validation and before saving.
        Example: attaching user info, logging, etc.
        """
        serializer.save()  # No user relation here, but you can customize if needed


# Update a book — only for authenticated users
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/<id>/update/
    Allows authenticated users to update an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Customize how updates are performed.
        """
        serializer.save()


# Delete a book — only for authenticated users
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<id>/delete/
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
