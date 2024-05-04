from typing import Set
import events

class Book:
    def __init__(self, id: str, title: str, authors: str, status: str = 'available', borrower: str = None):                                            
        self.id = id
        self.title = title
        self.status = status
        self.authors = authors
        self.borrower = borrower  # New attribute for storing MemberId
        self.events = []  # Initialize an empty list to store events

    def allocate_book(self, member_id: str):
        if self.status != 'available':
            raise ValueError(f"Book {self.id} is not available")
        
        self.status = 'borrowed'
        self.borrower = member_id
        self.events.append(events.BookBorrowed(book_id=self.id, member_id=member_id))

class Member:
    def __init__(self, id: str, name: str, surname: str):
        self.id = id
        self.name = name
        self.surname = surname
        self.allocated_books = set()  # store book_id
        self.events = []  # Initialize an empty list to store events


    def allocate_book(self, book_id: str):
        self.allocated_books.add(book_id)

    def return_book(self, book_id: str):
        self.allocated_books.discard(book_id)