import abc
from allocation.domain import model

class AbstractBookRepository(abc.ABC): #By inheriting from abc.ABC,
         #you make a class abstract, which means it cannot be instantiated on its own.

    @abc.abstractmethod      
    def addBook(self, item: model.Book):
        raise NotImplementedError
    
    @abc.abstractmethod
    def getBook(self, reference) -> model.Book:
        raise NotImplementedError

class SqlAlchemyBookRepository(AbstractBookRepository): 

    def __init__(self, session):
        self.session = session

    def addBook(self, book):
        self.session.add(book)

    def getBook(self, book_id):
        return self.session.query(model.Book).filter_by(id=book_id).one()
    
    def listBook(self):
        return self.session.query(model.Book).all()

class AbstractMemberRepository(abc.ABC):

    @abc.abstractmethod
    def add_member(self, member: model.Member):
        raise NotImplementedError

    @abc.abstractmethod
    def get_member(self, member_id) -> model.Member:
        raise NotImplementedError

class SqlAlchemyMemberRepository(AbstractMemberRepository):

    def __init__(self, session):
        self.session = session

    def add_member(self, member):
        self.session.add(member)

    def get_member(self, member_id):
        return self.session.query(model.Member).filter_by(id=member_id).one()
    
    def listMember(self):
        return self.session.query(model.Member).all()