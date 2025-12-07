class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    def is_old(self):
        return self.year < 2000

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year}) | ISBN: {self.isbn}"