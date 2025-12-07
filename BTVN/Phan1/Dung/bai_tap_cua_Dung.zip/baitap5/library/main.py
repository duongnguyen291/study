from models import Book
from utils import validate_isbn, validate_year

b1 = Book("5 Step to be SIGMA", "Anthony Nguyen", "1234567890123", 1936)
b2 = Book("My mom is kinda homeless", "IshowSpeed", "9876543210123", 2067)

books = [b1, b2]

for b in books:
    print(b)
    print("ISBN hợp lệ:", validate_isbn(b.isbn))
    print("Năm hợp lệ:", validate_year(b.year))
    print("Sách cũ:", b.is_old())
    print()