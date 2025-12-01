"""
Ví dụ sử dụng module database
File này import database.py và sử dụng các hàm của nó
"""

import database

print("=== BẮT ĐẦU CHƯƠNG TRÌNH CHÍNH ===")
print(f"Giá trị __name__ trong main.py = {__name__}")

# Sử dụng hàm từ database module
database.connect_db()
data = database.query_data()
print(f"Dữ liệu nhận được: {data}")

print("=== KẾT THÚC CHƯƠNG TRÌNH CHÍNH ===")

"""
Quan sát:
- Code trong if __name__ == "__main__" của database.py KHÔNG chạy
- Chỉ có code định nghĩa hàm và code ngoài if __name__ == "__main__" mới chạy
"""

