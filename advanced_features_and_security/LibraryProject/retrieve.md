# Retrieve Operation

from bookshelf.models import Book
book = Book.objects.get(title="1984")
print(book)

1984
George Orwell
1949
