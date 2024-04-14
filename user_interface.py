from Library import Library

class UserInterface:
    def __init__(self):
        self.library = Library()
        self.library.import_books("books.txt")
        self.library.import_users("users.txt")

    def main_menu(self):
        print("Welcome to the Library!")
        options = {"1": self.user_menu, "2": self.librarian_menu, "3": self.exit_program}
        while True:
            print("\nAre you a user or a librarian?")
            print("1. User")
            print("2. Librarian")
            print("3. Exit")
            choice = input("Enter the number of your choice: ")
            if choice in options:
                options[choice]()
            else:
                print("Invalid choice, please try again.")

    def user_menu(self):
        options = {"1": self.check_out_book, "2": self.return_book, "3": self.search_for_book,
                   "4": self.books_by_author, "5": self.books_by_genre, "6": self.list_checked_out_books,
                   "7": self.exit_program}
        while True:
            print("\nUser Menu")
            print("1. Check out a book")
            print("2. Return a book")
            print("3. Search for a book")
            print("4. See books by a specific author")
            print("5. See books in a specific genre")
            print("6. Checked out books")
            print("7. Exit")
            choice = input("Enter the number of your choice: ")
            if choice in options:
                options[choice]()
            else:
                print("Invalid choice, please try again.")

    def librarian_menu(self):
        options = {"1": self.library.add_book, "2": self.display_all_books, "3": self.library.add_user,
                   "4": self.display_all_users, "5": self.library.add_author, "6": self.display_all_authors,
                   "7": self.library.add_genre, "8": self.display_all_genres, "9": self.return_to_main}
        while True:
            print("\nLibrarian Menu")
            print("1. Add a book")
            print("2. Display all books")
            print("3. Add a user")
            print("4. Display all users")
            print("5. Add an author")
            print("6. Display all authors")
            print("7. Add a genre")
            print("8. Display all genres")
            print("9. Exit")
            choice = input("Enter the number of your choice: ")
            if choice in options:
                options[choice]()
            else:
                print("Invalid choice, please try again.")

    def exit_program(self):
        print("Goodbye!")
        self.library.export_data()
        exit()

    def return_to_main(self):
        print("Returning to main menu.")
        self.main_menu()

    def display_all_books(self):
        for book in self.library.books:
            print(book)

    def display_all_users(self):
        for user in self.library.users:
            print(user)

    def display_all_authors(self):
        for author in self.library.authors:
            print(author)

    def display_all_genres(self):
        for genre in self.library.genres:
            print(genre)

    def check_out_book(self):
        user_id = int(input("Enter your user ID: "))
        book_isbn = int(input("Enter the ISBN of the book you want to check out: "))
        user = self.library.get_user(user_id)
        book = self.library.get_book(book_isbn)
        if user is None:
            print("User not found.")
        elif book is None:
            print("Book not found.")
        else:
            self.library.check_out_book(user, book)
            print("Book checked out successfully.")

    def return_book(self):
        user_id = int(input("Enter your user ID: "))
        book_isbn = int(input("Enter the ISBN of the book you want to return: "))
        user = self.library.get_user(user_id)
        book = self.library.get_book(book_isbn)
        if user is None:
            print("User not found.")
        elif book is None:
            print("Book not found.")
        else:
            self.library.return_book(user, book)
            print("Book returned successfully.")

    def search_for_book(self):
        title = input("Enter the title of the book you are looking for: ")
        book = self.library.get_book_by_title(title)
        if book is None:
            print("Book not found.")
        else:
            print(book)

    def books_by_author(self):
        author_name = input("Enter the name of the author: ")
        books = self.library.get_books_by_author(author_name)
        if not books:
            print("No books found.")
        else:
            for book in books:
                print(book)

    def books_by_genre(self):
        genre_name = input("Enter the name of the genre: ")
        books = self.library.get_books_by_genre(genre_name)
        if not books:
            print("No books found.")
        else:
            for book in books:
                print(book)

    def list_checked_out_books(self):
        user_id = int(input("Enter your user ID: "))
        user = self.library.get_user(user_id)
        if user is None:
            print("User not found.")
        elif not user.books:
            print("No books checked out.")
        else:
            for book in user.books:
                print(book)