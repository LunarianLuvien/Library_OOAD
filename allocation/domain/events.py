# allocation/domain/events.py
from dataclasses import dataclass

@dataclass
class Event:
    pass

@dataclass
class BookBorrowed(Event):
    book_id: str
    member_id: str

@dataclass
class BookReturned(Event):
    book_id: str
    member_id: str