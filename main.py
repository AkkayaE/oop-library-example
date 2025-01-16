class Book:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        
        
    def book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Year: {self.year}")

book_1 = Book("Lord of the Rings", "J.R.R. Tolkien", "fantastic", 2002)
book_2 = Book("Animal Farm", "George Orwell", "fable", 1945)

class Library:
    def __init__(self, address, hours):
        self.address = address
        self.hours = hours
        
        def library_info(self):
            print(f"Address: {self.address}")
            print(f"Hours: {self.hours}")

library_a = Library("Rejtana 16", 09.00-21.00)
library_b = Library("Suwak", 7/24)

from book import Book
from library import Library


