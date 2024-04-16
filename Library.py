import random
import re
from Book import Book
from User import User
from Author import Author
from Genre import Genre

class Library:
    def __init__(self, books=None, users=None, authors=None, genres=None):
        self.books = books if books is not None else []
        self.users = users if users is not None else []
        self.authors = authors if authors is not None else []
        self.genres = genres if genres is not None else []
        self.used_ids = set(u.id for u in self.users)
        self.used_isbns = set(b.ISBN for b in self.books)

    # Get Methods
    def get_user_by_name(self, name):
        return next((user for user in self.users if user.name.lower() == name.lower()), None)
    
    def get_book_by_title(self, title):
        title = title.lower()
        return next((book for book in self.books if book.title.lower() == title), None)

    def get_author(self, name):
        return next((author for author in self.authors if author.name.lower() == name.lower()), None)

    def get_genre(self, name):
        return next((genre for genre in self.genres if genre.genre_name.lower() == name.lower()), None)

    def get_books_by_author(self, author_name):
        return [book for book in self.books if book.author.name.lower() == author_name.lower()]

    def get_books_by_genre(self, genre_name):
        return [book for book in self.books if book.genre.genre_name.lower() == genre_name.lower()]

    def get_checked_out_books(self, user):
        return [book for book in user.books if not book.availability]
    
    def get_book_by_isbn(self, isbn):
        return next((book for book in self.books if book.ISBN == isbn), None)


    # Add Methods
    def add_user(self, name):
        user_id = random.randint(1000, 9999)
        while user_id in self.used_ids:
            user_id = random.randint(1000, 9999)
        new_user = User(name, user_id)
        self.users.append(new_user)
        self.used_ids.add(user_id)
        return new_user

    def add_book(self, title, author, genre, publication_date, isbn):
        new_book = Book(title, author, genre, publication_date, isbn, True)
        self.books.append(new_book)
        self.used_isbns.add(isbn)
        return new_book

    def add_author(self, author_name):
        new_author = Author(author_name)
        self.authors.append(new_author)
        return new_author

    def add_genre(self, genre_name, description):
        new_genre = Genre(genre_name, description)
        self.genres.append(new_genre)
        return new_genre

    # Check-out and Return Methods
    def check_out_book(self, user, book):
        if book.availability:
            book.availability = False
            user.books.append(book)
            return True
        return False

    def return_book(self, user, book):
        if book in user.books:
            book.availability = True
            user.books.remove(book)
            return True
        return False

    # Import/Export Data Methods
    def import_users(self):
        print("Starting to import users...")
        try:
            with open("users.txt", "r") as file:
                line_count = 0
                for line in file:
                    line_count += 1
                    line = line.strip()
                    if not line:  # Skip empty lines
                        continue
                    parts = line.split(", ")
                    if len(parts) < 2:
                        print(f"Skipping malformed line #{line_count}: '{line}'")
                        continue

                    name = parts[0].strip()
                    user_id_str = ''.join(filter(str.isdigit, parts[1].strip()))  # Extract digits only

                    if not user_id_str:  # Check if there are any digits at all
                        print(f"Skipping line due to invalid user ID format on line #{line_count}: '{line}'")
                        continue
                    user_id = int(user_id_str)

                    checked_out_isbns = []
                    if len(parts) > 2:
                        isbn_parts = parts[2].split(',')
                        for isbn_str in isbn_parts:
                            isbn_clean = ''.join(filter(str.isdigit, isbn_str.strip()))  # Clean and extract digits
                            if isbn_clean:  # Check if the cleaned string has any digits
                                checked_out_isbns.append(int(isbn_clean))
                            else:
                                print(f"Invalid ISBN format found and ignored on line #{line_count}: '{isbn_str}'")

                    if user_id not in self.used_ids:
                        new_user = User(name, user_id)
                        self.users.append(new_user)
                        self.used_ids.add(user_id)
                        #print(f"Added user: {new_user}")

                        # Restore checked-out books based on ISBNs
                        for isbn in checked_out_isbns:
                            book = self.get_book_by_isbn(isbn)
                            if book:
                                book.availability = False
                                new_user.books.append(book)
        except FileNotFoundError:
            print("User file not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def import_books(self):
        try:
            with open("books.txt", "r") as file:
                for line in file:
                    title, author_name, genre_name, publication_date, ISBN, availability = line.strip().split(", ")
                    ISBN = int(ISBN)
                    availability = availability == "True"
                    author = self.get_author(author_name) or self.add_author(author_name)
                    genre = self.get_genre(genre_name) or self.add_genre(genre_name, "Default description")
                    new_book = Book(title, author, genre, publication_date, ISBN, availability)
                    self.books.append(new_book)
                    self.used_isbns.add(ISBN)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def export_data(self):
        self.save_users()
        self.save_books()

    def save_users(self):
        with open("users.txt", "w") as file:
            for user in self.users:
                # Collect ISBNs of checked-out books to a list
                checked_out_isbns = [str(book.ISBN) for book in user.books if not book.availability]
                # Format the user data with ISBNs correctly
                user_data = f"{user.name}, {user.id}"
                if checked_out_isbns:
                    user_data += ", " + ",".join(checked_out_isbns)
                file.write(user_data + "\n")

    def save_books(self):
        with open("books.txt", "w") as file:
            for book in self.books:
                availability = "True" if book.availability else "False"
                file.write(f"{book.title}, {book.author.name}, {book.genre.genre_name}, {book.publication_date}, {book.ISBN}, {availability}\n")
