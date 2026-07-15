# Refactoring Prompt

Act as a Python refactoring agent.
I have procedural code for a small library system.
Refactor it into Object-Oriented Programming using classes.
Keep the behavior the same and do not add new features.
Create a Book class with title, author, year, and available attributes.
Build those Book attributes in __init__.
Create a Library class with a name attribute and a books list.
Build the Library name and books list in __init__.
Turn add_book, remove_book, search_by_author, checkout_book, return_book, and get_available_books into Library methods.
Keep the method names in snake_case exactly as written.
Use self as the first parameter for every Library method.
Explain how the refactor changes global data into object state.

# OOP Analysis

The refactored version improves encapsulation because each Book stores its own attributes and the Library owns its collection of books.
The procedural version depends on global variables, while the OOP version moves that state into objects created with __init__.
The six operations become methods on Library, and each method uses self to access the correct library instance.
This keeps the behavior similar while making the relationship between data and actions clearer.

# Reflection

Using AI for refactoring is useful, but code review is still necessary to confirm that names, behavior, and constraints were preserved.
This refactoring improves maintainability because future changes can focus on the Book and Library classes instead of shared global state.
