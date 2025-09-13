from django.urls import path
from .views import list_books, LibraryDetailView   # ← add list_books here


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
