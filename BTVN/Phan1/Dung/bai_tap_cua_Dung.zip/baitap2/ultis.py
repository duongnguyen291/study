def format_currency(amount):
    return f"{amount:,} VNĐ"

def validate_email(email):
    return "@" in email and "." in email

# Chỉ chạy khi file này được chạy trực tiếp
if __name__ == "__main__":
    print("=== TEST UTILS ===")
    print(format_currency(100000))
    print(validate_email("abc@gmail.com"))