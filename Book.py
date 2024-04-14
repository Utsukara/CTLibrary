class Book:
    def __init__(self, title, author, genre, publication_date, ISBN, availability):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_date = publication_date
        self.ISBN = ISBN
        self.availability = availability

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Publication Date: {self.publication_date}, ISBN: {self.ISBN}, Availability: {self.availability}"
