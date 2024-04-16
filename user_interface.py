import random
import datetime
from Library import Library

class UserInterface:
    def __init__(self):
        self.library = Library()
        self.library.import_books()
        self.library.import_users()
        self.current_user = None

    # Main Menu
    def main_menu(self):
        print("Welcome to the Library!")
        while True:
            print("\nAre you a user or a librarian?")
            print("1. User")
            print("2. Librarian")
            print("3. Exit")
            choice = input("Enter the number of your choice: ")
            if choice == "1":
                self.user_login()
            elif choice == "2":
                self.librarian_login()
            elif choice == "3":
                self.exit_program()
            else:
                print("Invalid choice, please try again.")

    # Login Methods
    def user_login(self):
        user_name = input("Please enter your user name: ")
        user = self.library.get_user_by_name(user_name)
        if user is None:
            print("User not found, creating a new user.")
            user = self.library.add_user(user_name)
        self.current_user = user
        print(f"Welcome, {user.name}!")
        self.user_menu()

    def librarian_login(self):
        password = input("Please enter the librarian password: ")
        if password == "librarian":
            print("Access granted.")
            self.librarian_menu()
        else:
            print("Access denied. Incorrect password.")

    # User Menu
    def user_menu(self):
        options = {
            "1": self.check_out_book,
            "2": self.return_book,
            "3": self.display_all_books,
            "4": self.search_for_book,
            "5": self.books_by_author,
            "6": self.books_by_genre,
            "7": self.list_checked_out_books,
            "8": self.current_user_details,
            "9": self.exit_program
        }
        while True:
            print("\nUser Menu")
            print("1. Check out a book")
            print("2. Return a book")
            print("3. Display all books")
            print("4. Search for a book")
            print("5. See books by a specific author")
            print("6. See books in a specific genre")
            print("7. See your checked out books")
            print("8. User Details")
            print("9. Exit")
            choice = input("Enter the number of your choice: ")
            action = options.get(choice)
            if action:
                action()
            else:
                print("Invalid choice, please try again.")

    # Librarian Menu
    def librarian_menu(self):
        options = {
            "1": self.add_book,
            "2": self.add_author,
            "3": self.add_genre,
            "4": self.display_all_books,
            "5": self.display_all_users,
            "6": self.display_all_authors,
            "7": self.display_all_genres,
            "8": self.change_genre_description,
            "9": self.return_to_main
        }
        while True:
            print("\nLibrarian Menu")
            print("1. Add a book")
            print("2. Add an author")
            print("3. Add a genre")
            print("4. Display all books")
            print("5. Display all users")
            print("6. Display all authors")
            print("7. Display all genres")
            print("8. Change genre description")
            print("9. Return to main menu")
            choice = input("Enter the number of your choice: ")
            action = options.get(choice)
            if action:
                action()
            else:
                print("Invalid choice, please try again.")

    # Actions for Users
    def check_out_book(self):
        book_title = input("Enter the title of the book you want to check out: ")
        book = self.library.get_book_by_title(book_title)
        if book and book.availability:
            result = self.library.check_out_book(self.current_user, book)
            if result:
                print("Book checked out successfully.")
            else:
                print("Failed to check out book.")
        else:
            print("Book not found or already checked out.")

    def return_book(self):
        book_title = input("Enter the title of the book you want to return: ")
        book = self.library.get_book_by_title(book_title)
        if book and not book.availability:
            result = self.library.return_book(self.current_user, book)
            if result:
                print("Book returned successfully.")
            else:
                print("Failed to return book.")
        else:
            print("Book not found or not checked out.")

    # Actions for Librarians
    def add_book(self):
        title = input("Enter the title of the book: ")
        existing_book = self.library.get_book_by_title(title)
        if existing_book:
            print("This book already exists in the library.")
            return
        isbn = random.randint(1000000000, 9999999999)
        while isbn in self.library.used_isbns:
            isbn = random.randint(1000000000, 9999999999)
        author_name = input("Enter the name of the author: ")
        author = self.library.get_author(author_name)
        if not author:
            print("Author not found, adding a new author.")
            author = self.add_author(author_name)
        genre_name = input("Enter the genre of the book: ")
        genre = self.library.get_genre(genre_name)
        if not genre:
            print("Genre not found, adding a new genre.")
            description = input("Enter a description for the new genre: ")
            genre = self.add_genre(genre_name, description)
        publication_year = self.get_valid_publication_year()
        new_book = self.library.add_book(title, author, genre, publication_year, isbn)
        print(f"Book added successfully: {new_book}")

    def add_author(self, author_name=None):
        if not author_name:
            author_name = input("Enter the name of the author: ")
        existing_author = self.library.get_author(author_name)
        if existing_author:
            print("This author already exists.")
            return existing_author
        new_author = self.library.add_author(author_name)
        print(f"Author added successfully: {new_author}")
        return new_author

    def add_genre(self, genre_name=None, description=None):
        if not genre_name:
            genre_name = input("Enter the name of the genre: ")
        if not description:
            print("Would you like to add a description for the genre? (yes/no)")
            if input().lower().startswith('y'):
                description = input("Enter the description of the genre: ")
            else:
                description = "No description provided."
        existing_genre = self.library.get_genre(genre_name)
        if existing_genre:
            print("This genre already exists.")
            return existing_genre
        new_genre = self.library.add_genre(genre_name, description)
        print(f"Genre added successfully: {new_genre}")
        return new_genre

    def display_all_books(self):
        if self.library.books:
            for index, book in enumerate(self.library.books, 1):
                print(f"{index}. {book}")
        else:
            print("No books currently registered in the library.")

    def display_all_users(self):
        if self.library.users:
            print("Registered users:")
            for user in self.library.users:
                print(user)
        else:
            print("No users currently registered.")


    def display_all_authors(self):
        if self.library.authors:
            for author in self.library.authors:
                print(author)
        else:
            print("No authors currently registered.")

    def display_all_genres(self):
        if self.library.genres:
            for genre in self.library.genres:
                print(genre)
        else:
            print("No genres currently registered.")

    def change_genre_description(self):
        genre_name = input("Enter the genre name whose description you want to change: ")
        genre = self.library.get_genre(genre_name)
        if genre:
            new_description = input("Enter the new description: ")
            genre.description = new_description
            print("Genre description updated successfully.")
        else:
            print("Genre not found.")

    def current_user_details(self):
        if self.current_user:
            print(self.current_user)
        else:
            print("No user is currently logged in.")

    def get_valid_publication_year(self):
        current_year = datetime.datetime.now().year
        while True:
            year_input = input("Enter the publication year (YYYY): ")
            if year_input.isdigit() and len(year_input) == 4:
                year = int(year_input)
                if 1800 <= year <= current_year:
                    return year
                else:
                    print(f"Please enter a year between 1800 and {current_year}.")
            else:
                print("Invalid year format. Please enter a four-digit year (e.g., 2021).")

    def search_for_book(self):
        search_term = input("Enter a search term: ")
        results = self.library.search_books(search_term)
        if results:
            for index, book in enumerate(results, 1):
                print(f"{index}. {book}")
        else:
            print("No results found.")

    def books_by_author(self):
        author_name = input("Enter the name of the author: ")
        author = self.library.get_author(author_name)
        if author:
            results = self.library.get_books_by_author(author)
            for index, book in enumerate(results, 1):
                print(f"{index}. {book}")
        else:
            print("Author not found.")

    def books_by_genre(self):
        genre_name = input("Enter the name of the genre: ")
        genre = self.library.get_genre(genre_name)
        if genre:
            results = self.library.get_books_by_genre(genre)
            for index, book in enumerate(results, 1):
                print(f"{index}. {book}")
        else:
            print("Genre not found.")

    def list_checked_out_books(self):
        checked_out_books = self.library.get_checked_out_books(self.current_user)
        if checked_out_books:
            for index, book in enumerate(checked_out_books, 1):
                print(f"{index}. {book}")
        else:
            print("No books currently checked out.")

    def exit_program(self):
        print("Goodbye!")
        self.library.export_data()
        exit()

    def return_to_main(self):
        self.main_menu()
