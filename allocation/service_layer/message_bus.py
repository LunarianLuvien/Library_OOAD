from typing import List, Dict, Callable, Type
from allocation.adapters import email
from allocation.domain import events
import handlers

def handle(event: events.Event, uow):
    for handler in HANDLERS[type(event)]:
        handler(event,uow)

def send_book_borrowed_notification(event: events.BookBorrowed):
    email.send_mail(
        "library@domain.com",
        f"Book {event.book_id} borrowed by member {event.member_id}"
    )

def send_book_returned_notification(event: events.BookReturned):
    email.send_mail(
        "library@domain.com",
        f"Book {event.book_id} returned by member {event.member_id}"
    )

HANDLERS = {
    events.BookBorrowed: [handlers.allocate_book_to_member],
    events.BookReturned: [send_book_returned_notification],
}  # type: Dict[Type[events.Event], List[Callable]]