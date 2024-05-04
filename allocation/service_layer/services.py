from allocation.domain import model
from allocation.service_layer import unit_of_work
from allocation.service_layer import message_bus
from allocation.domain import events


def add_book(id: str, title: str, authors: str, uow: unit_of_work.AbstractBookUnitOfWork):
    with uow:
        uow.books.addBook(model.Book(id, title, authors))  # uow.books is defined in AbstractBookUnitOfWork   
        uow.commit()

def add_member(id: str, name: str, surname: str, uow: unit_of_work.AbstractMemberUnitOfWork):
    with uow:
        uow.members.add_member(model.Member(id, name, surname))  # Adjusted for Member domain model changes
        uow.commit()

def borrow_books(member_id: str, book_id: str, book_uow: unit_of_work.AbstractBookUnitOfWork):
    with book_uow:
        book = book_uow.books.getBook(book_id)
        if not book:
            raise ValueError(f"Book {book_id} not found")
        
        book.allocate_book(member_id)
        
        for event in book.events:
            message_bus.handle(event, book_uow)

        book_uow.commit()
