class Book:
    def __init__(self, title, author, publish_date, edition, status="Available"):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.edition = edition
        self.status = status
        self.borrower = None
        self.due_date = None

class User:
    def __init__(self, username):
        self.username = username

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book: {book.title}")

    def search_books(self, criteria):
        results = []
        for book in self.books:
            if criteria.lower() in book.title.lower() or criteria.lower() in book.author.lower():
                results.append(book)
        if results:
            print("Search results:")
            for book in results:
                print(f"Title: {book.title}, Author: {book.author}")
        else:
            print("No matching books found.")

    def borrow_book(self, user, book_title, due_date):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                if book.status == "Available":
                    book.status = "Borrowed"
                    book.borrower = user
                    book.due_date = due_date
                    print(f"{user.username} borrowed {book.title}. Due date: {book.due_date}")
                else:
                    print(f"Sorry, {book.title} is not available for borrowing.")
                return
        print(f"Book with title '{book_title}' not found in the library.")

    def return_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                if book.status == "Borrowed":
                    book.status = "Available"
                    book.borrower = None
                    book.due_date = None
                    print(f"Returned {book.title}")
                else:
                    print(f"{book.title} is not currently borrowed.")
                return
        print(f"Book with title '{book_title}' not found in the library.")

    def display_books(self):
        if self.books:
            print("Library books:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, Status: {book.status}")
        else:
            print("The library is empty.")

library = Library()

while True:
    print("\nOptions:")
    print("1. Add a new book")
    print("2. Search for a book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Display book information")
    print("6. Update book information")
    print("7. Quit")
    
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        title = input("Enter the book title: ")
        author = input("Enter the author's name: ")
        publish_date = input("Enter the publish date YYYY-MM-DD: ")
        edition = input("Enter the edition: ")

        if title and author and publish_date and edition:
            new_book = Book(title, author, publish_date, edition)
            library.add_book(new_book)
        else:
            print("Invalid input. Please provide all required information.")

    elif choice == "2":
        search_criteria = input("Enter search criteria (title or author): ")
        library.search_books(search_criteria)

    elif choice == "3":
        username = input("Enter your username: ")
        user = User(username)
        book_title = input("Enter the title of the book you want to borrow: ")
        due_date = input("Enter the due date (YYYY-MM-DD): ")

        if username and user and book_title and due_date:
            library.borrow_book(user, book_title, due_date)
        else:
            print("Invalid input. Please provide all required information.")

    elif choice == "4":
        book_title = input("Enter the title of the book you want to return: ")

        if book_title:
            library.return_book(book_title)
        else:
            print("Invalid input. Please provide the title of the book.")

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        book_title = input("Enter the title of the book you want to update: ")

        if book_title:
            for book in library.books:
                if book.title.lower() == book_title.lower():
                    new_title = input("Enter the new title (press Enter to keep the current title): ")
                    new_author = input("Enter the new author (press Enter to keep the current author): ")
                    new_publish_date = input("Enter the new publish date (press Enter to keep the current publish date): ")
                    new_edition = input("Enter the new edition (press Enter to keep the current edition): ")

                    if new_title:
                        book.title = new_title
                    if new_author:
                        book.author = new_author
                    if new_publish_date:
                        book.publish_date = new_publish_date
                    if new_edition:
                        book.edition = new_edition

                    print(f"Updated book information for {book.title}.")
                    break
            else:
                print(f"Book with title '{book_title}' not found in the library.")

    elif choice == "7":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter a valid number (1-7).")
