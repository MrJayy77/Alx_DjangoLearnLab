# Retrieve Operation

We created a book titled "1984" by George Orwell.

**Command:**
```python
from bookshelf.models import Book
list(Book.objects.values_list("title", flat=True))
