class Genre:
    def __init__(self, genre_name, description, books=None):
        self.genre_name = genre_name
        self.description = description
        self.books = books if books is not None else []

    def __str__(self):
        return f"Genre: {self.genre_name}, Description: {self.description}"
