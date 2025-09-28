from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve a single book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update a book (requires book ID)
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book (requires book ID)
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
