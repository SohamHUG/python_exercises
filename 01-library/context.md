# Context:
You need to create a Python program to manage book loans in a small library.

## Part 1 - Data Structures
- Create a books dictionary with at least 5 books in the following format:
```python
{
    "001": {"title": "The Little Prince", "author": "Saint-Exupéry", "available": True},
    "002": {"title": "1984", "author": "George Orwell", "available": False},
    ...
}
```

- Create a users list with at least 3 users:
```python
[
    {"id": 1, "name": "Alice", "borrowed_books": []},
    {"id": 2, "name": "Bob", "borrowed_books": ["002"]},
    ...
]
```

## Part 2 - Functions
#### Implement the following functions:

`borrow_book(user_id, book_id)` :
- Checks if the book is available
- Updates the book’s status
- Adds the book to the user’s borrowed list
- Returns a confirmation/error message

`return_book(user_id, book_id)` :
- Performs the inverse operation of `borrow_book`

`display_status()` : 
- Number of books available/borrowed
- List of users with their borrowed books