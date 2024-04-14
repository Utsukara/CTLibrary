class User:
    def __init__(self, name, id, books=None):
        self.name = name
        self.id = id
        self.books = books if books is not None else []

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}"
