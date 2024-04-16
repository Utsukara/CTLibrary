class User:
    def __init__(self, name, id, books=None):
        self.name = name
        self.id = id
        self.books = books if books else []

    def __str__(self):
        return f"User Name: {self.name}, ID: {self.id}, Books Checked Out: {len(self.books)}"

