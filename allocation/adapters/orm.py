from sqlalchemy import (
    Table, MetaData, Column, String, Integer, ForeignKey
)
from sqlalchemy.orm import registry, relationship
from sqlalchemy import create_engine
from allocation.domain import model
from sqlalchemy import event

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

books = Table(
    "books",
    metadata,
    Column("id", String(50), primary_key=True),
    Column("title", String(255)),
    Column("status", String(60)),
    Column("authors", String(255)),
    Column("borrower", String(50), nullable=True)  
)

members = Table(
    "members",
    metadata,
    Column("id", String(50), primary_key=True),
    Column("name", String(100)),
    Column("surname", String(100))
)

member_books = Table(
    "member_books",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("member_id", String(50), ForeignKey("members.id")),
    Column("book_id", String(50), ForeignKey("books.id"), unique=True)
)

def start_mappers():
    mapper_registry.map_imperatively(
        model.Book,
        books,
        properties={
            # Map the borrower column to the Book class
            'borrower': books.c.borrower
        }
    )
    mapper_registry.map_imperatively(
        model.Member,
        members,
        properties={
            "allocated_books": relationship(
                model.Book,
                secondary=member_books,
                collection_class=set,
                viewonly=True
            )
        },
    )

def create_tables(database_uri="sqlite:///mydatabase.db"):
    engine = create_engine(database_uri, echo=True)
    metadata.create_all(engine)
    print("Tables created")  # Debug    


@event.listens_for(model.Book, "load")
def receive_load(book, _):
    book.events = []