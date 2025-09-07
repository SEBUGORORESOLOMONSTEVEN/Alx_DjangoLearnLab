import os
import sys

# Add your Django project's root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create sample data
author1 = Author.objects.create(name="J.R.R. Tolkien")
author2 = Author.objects.create(name="J.K. Rowling")

book1 = Book.objects.create(title="The Hobbit", author=author1)
book2 = Book.objects.create(title="The Lord of the Rings", author=author1)
book3 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author2)

library1 = Library.objects.create(name="City Library")
library1.books.add(book1, book3)

librarian1 = Librarian.objects.create(name="Ms. Davis", library=library1)

# Query all books by a specific author
print("Query 1: Books by J.R.R. Tolkien")
tolkien_books = Book.objects.filter(author__name="J.R.R. Tolkien")
for book in tolkien_books:
    print(f"- {book.title}")

print("\n")

# List all books in a library
print("Query 2: Books in City Library")
city_library = Library.objects.get(name="City Library")
library_books = city_library.books.all()
for book in library_books:
    print(f"- {book.title}")

print("\n")

# Retrieve the librarian for a library
print("Query 3: Librarian for City Library")
try:
    city_library_librarian = city_library.librarian
    print(f"- The librarian is {city_library_librarian.name}")
except Librarian.DoesNotExist:
    print("- No librarian found for this library.")
