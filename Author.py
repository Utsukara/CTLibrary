class Author:
    def __init__(self, name, books=None):
        self.name = name
        self.books = books if books is not None else []

    def __str__(self):
        return f"Author: {self.name}"