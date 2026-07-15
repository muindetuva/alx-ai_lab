class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)
        return len(self.books)

    def remove_book(self, title):
        for i in range(len(self.books)):
            if self.books[i].title == title:
                self.books.pop(i)
                return True
        return False

    def search_by_author(self, author):
        results = []
        for book in self.books:
            if book.author == author:
                results.append(book)
        return results

    def checkout_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                return True
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title and not book.available:
                book.available = True
                return True
        return False

    def get_available_books(self):
        available = []
        for book in self.books:
            if book.available:
                available.append(book)
        return available
