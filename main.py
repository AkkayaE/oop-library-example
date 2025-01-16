from book import Book
from library import Library


book_1 = Book("Lord of the Rings", "J.R.R. Tolkien", "fantastic", 2002)
book_2 = Book("Animal Farm", "George Orwell", "fable", 1945)


library_a = Library("Rejtana 16", 09.00-21.00)
library_b = Library("Suwak", 7/24)

print(book_1.title)
print(book_1.author)
print(book_1.genre)
print(book_1.year)

print(library_b.address)
print(library_b.hours)
