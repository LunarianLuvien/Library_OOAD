from allocation.domain import model, events
from allocation.adapters import repository

def allocate_book_to_member(event: events.BookBorrowed, uow: repository.AbstractMemberUnitOfWork):
    with uow:
        member = uow.members.get_member(event.member_id)
        if not member:
            raise ValueError("Member not found")

        book = uow.books.getBook(event.book_id)
        if not book:
            raise ValueError("Book not found")

        member.allocate_book(event.book_id)
        uow.commit()