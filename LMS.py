class Book:
    def __init__(self, title, author, id, available=True):
        self.title = title
        self.author = author
        self.id = id
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} (ID: {self.id})"

    def set_availability(self, availability):
        self.available = availability

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, id):
        for book in self.books:
            if book.id == id:
                return book
        return None

    def add_member(self, member):
        self.members.append(member)

    def find_member(self, id):
        for member in self.members:
            if member.id == id:
                return member
        return None

    def borrow_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        if book and member and book.available:
            book.set_availability(False)
            member.borrow_book(book)
            return True
        return False

    def return_book(self, book_id, member_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        if book and member and not book.available:
            book.set_availability(True)
            member.return_book(book)
            return True
        return False

class Member:
    def __init__(self, id, name, subscribed=True):
        self.id = id
        self.name = name
        self.subscribed = subscribed
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

    def __str__(self):
        return f"{self.name} (ID: {self.id}, Subscribed: {self.subscribed})"
