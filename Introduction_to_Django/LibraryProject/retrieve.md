# Retrieve Operation

from bookshelf.models import Book
books = Book.objects.all()
print(list(books.values_list("title", flat=True)))  # ["1984"]
