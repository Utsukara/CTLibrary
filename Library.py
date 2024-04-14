import random
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

    def add_book(self):
        book_title = input("Enter the title of the book: ")
        author_name = input("Enter the author of the book: ")
        genre_name = input("Enter the genre of the book: ")
        book_publication_date = input("Enter the publication date of the book: ")
        book_ISBN = random.randint(1, 999999999)
        while book_ISBN in self.used_isbns:
            book_ISBN = random.randint(1, 999999999)

        # Find or create author
        author = self.get_author(author_name)
        if not author:
            author = Author(author_name)
            self.authors.append(author)

        # Find or create genre
        genre = self.get_genre(genre_name)
        if not genre:
            genre = Genre(genre_name, description=input("Enter the description of the genre: "))
            self.genres.append(genre)

        book_availability = True
        new_book = Book(book_title, author, genre, book_publication_date, book_ISBN, book_availability)
        self.books.append(new_book)
        self.used_isbns.add(book_ISBN)
        print("Book added successfully!")

    def get_author(self, name):
        for author in self.authors:
            if author.name == name:
                return author
        return None

    def get_genre(self, name):
        for genre in self.genres:
            if genre.genre_name == name:
                return genre
        return None

    def add_user(self):
        user_name = input("Enter the name of the user: ")
        user_id = random.randint(1, 999999999)
        while user_id in self.used_ids:
            user_id = random.randint(1, 999999999)
        new_user = User(user_name, user_id)
        self.users.append(new_user)
        self.used_ids.add(user_id)

    def add_author(self):
        author_name = input("Enter the name of the author: ")
        new_author = Author(author_name)
        self.authors.append(new_author)

    def add_genre(self):
        genre_name = input("Enter the name of the genre: ")
        new_genre = Genre(genre_name)
        self.genres.append(new_genre)

    def check_out_book(self, user, book):
        if book.availability:
            book.availability = False
            user.books.append(book)
            print("Book checked out successfully!")
        else:
            print("Book not available.")

    def return_book(self, user, book):
        if book in user.books:
            book.availability = True
            user.books.remove(book)
            print("Book returned successfully!")
        else:
            print("Book not found or already returned.")

    def save_users(self):
        with open("users.txt", "w") as file:
            for user in self.users:
                file.write(f"{user.name}, {user.id}\n")

    def save_books(self):
        with open("books.txt", "w") as file:
            for book in self.books:
                availability = "True" if book.availability else "False"
                file.write(f"{book.title}, {book.author.name}, {book.genre.genre_name}, {book.publication_date}, {book.ISBN}, {availability}\n")


def import_users(self):
    try:
        with open("users.txt", "r") as file:
            for line in file:
                name, id = line.strip().split(", ")
                id = int(id)  # Convert ID to integer
                if id not in self.used_ids:
                    new_user = User(name, id)
                    self.users.append(new_user)
                    self.used_ids.add(id)
    except FileNotFoundError:
        print("User file not found.")
    except ValueError:
        print("Error in data format for users.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def import_books(self):
    try:
        with open("books.txt", "r") as file:
            for line in file:
                title, author_name, genre_name, publication_date, ISBN, availability = line.strip().split(", ")
                ISBN = int(ISBN)
                availability = availability == "True"

                if ISBN not in self.used_isbns:
                    author = self.get_author(author_name) or Author(author_name)
                    if not self.get_author(author_name):
                        self.authors.append(author)

                    genre = self.get_genre(genre_name) or Genre(genre_name, description="Default description")
                    if not self.get_genre(genre_name):
                        self.genres.append(genre)

                    new_book = Book(title, author, genre, publication_date, ISBN, availability)
                    self.books.append(new_book)
                    self.used_isbns.add(ISBN)
    except FileNotFoundError:
        print("Book file not found.")
    except ValueError:
        print("Error in data format for books.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    def export_data(self):
        self.save_users()
        self.save_books()