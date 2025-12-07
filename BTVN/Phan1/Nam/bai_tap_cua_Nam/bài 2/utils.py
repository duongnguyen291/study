def format_currency(amount):
    return f"{amount:,.0f} VND"

def validate_email(email):
    return "@" in email and "." in email
if __name__ == "__main__":
    print(format_currency(100000))

    print(validate_email("test@gmail.com"))
