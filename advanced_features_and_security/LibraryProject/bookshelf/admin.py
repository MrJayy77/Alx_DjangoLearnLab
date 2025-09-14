from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields as columns in the list view
    list_display = ("title", "author", "publication_year")

    # Add a search bar (search by title or author)
    search_fields = ("title", "author")

    # Add filter sidebar (filter by year of publication)
    list_filter = ("publication_year",)
