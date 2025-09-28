from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # GET: List all books
    path('books/', BookListView.as_view(), name='book-list'),

    # GET: Retrieve details of a single book by ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # POST: Create a new book (Authenticated users only)
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # PUT/PATCH: Update a specific book (Authenticated users only)
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # DELETE: Delete a specific book (Authenticated users only)
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
