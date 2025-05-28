books = {
    "001": {"title": "Le Petit Prince", "author": "Saint-Exupéry", "available": True},
    "002": {"title": "1984", "author": "George Orwell", "available": False},
    "003": {"title": "Harry Potter à l'école des sorciers", "author": "J.K. Rowling", "available": True},
    "004": {"title": "Le Seigneur des Anneaux", "author": "J.R.R. Tolkien", "available": False},
    "005": {"title": "Fondation", "author": "Isaac Asimov", "available": False},
}

users = [
    {"id": 1, "name": "Alice", "books_list": []},
    {"id": 2, "name": "Bob", "books_list": ["002"]},
    {"id": 3, "name": "John", "books_list": ["004", "005"]},
]

def borrow_book(id_user, id_book):   
    try:
        user = next((u for u in users if u["id"] == id_user), None)
        
        if not user:
            print("User not found")
            return False
        
        if books[id_book]["available"] == True:
            books[id_book]["available"] = False
            user["books_list"].append(id_book)
            print("Book successfully borrowed")
            return True
        
        else:
            print("Book not available")
            return False
    except KeyError:
        print("Book not found")
        return False


def return_book(id_user, id_book,):
    try: 
        user = next((u for u in users if u["id"] == id_user), None)
        
        if not user:
            print("Utilisateur non trouvé")
            return False

        if not books[id_book]["available"]:
            books[id_book]["available"] = True
            user["books_list"].remove(id_book)
            return True
        else:
            print("This book is not in your list")
            return False
    except KeyError:
        print("Book not found")
        return False


def display_status():          
    available_count = sum(1 for book in books.values() if book["available"])
    print("Number of books available :", available_count)
    print("Livres disponibles :")
    for book in books.values():
        if book["available"]:
            print(f"  - {book['title']} de {book['author']}")


    unavailable_count = sum(1 for book in books.values() if not book["available"])
    print("Number of borrowed books :", unavailable_count)

    print("\nUsers and their books :")

    for user in users:
        print(f"  - {user['name']} : {[books[bid]['title'] for bid in user['books_list']]}")


display_status()
borrow_book(3, "003")
display_status()
return_book(3, "004")
display_status()