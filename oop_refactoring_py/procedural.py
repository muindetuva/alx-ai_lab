# Library system - procedural style
library_name = "City Library"
books = []

def add_book(title, author, year):
    book = {"title": title, "author": author, "year": year, "available": True}
    books.append(book)
    return len(books)

def remove_book(title):
    for i in range(len(books)):
        if books[i]["title"] == title:
            books.pop(i)
            return True
    return False

def search_by_author(author):
    results = []
    for book in books:
        if book["author"] == author:
            results.append(book)
    return results

def checkout_book(title):
    for book in books:
        if book["title"] == title and book["available"]:
            book["available"] = False
            return True
    return False

def return_book(title):
    for book in books:
        if book["title"] == title and not book["available"]:
            book["available"] = True
            return True
    return False

def get_available_books():
    available = []
    for book in books:
        if book["available"]:
            available.append(book)
    return available
