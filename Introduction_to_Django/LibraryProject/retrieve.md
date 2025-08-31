# Retrieve Operation

**Command:**
```python
from bookshelf.models import Book
list(Book.objects.values_list("title", flat=True))
