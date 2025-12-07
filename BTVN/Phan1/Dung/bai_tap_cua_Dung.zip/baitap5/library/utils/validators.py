def validate_isbn(isbn):
    return len(isbn) == 13

def validate_year(year):
    return 1900 <= year <= 2024