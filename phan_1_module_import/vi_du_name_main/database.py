"""
Ví dụ về if __name__ == "__main__"
File này minh họa cách một file vừa có thể chạy độc lập, vừa có thể làm thư viện
"""


def connect_db():
    """Hàm kết nối Database"""
    print("Đang kết nối Database...")
    return True


def query_data():
    """Hàm truy vấn dữ liệu"""
    print("Đang truy vấn dữ liệu...")
    return ["data1", "data2", "data3"]


# Đoạn code test, chỉ chạy khi developer đang sửa file này
# (tức là chạy trực tiếp: python database.py)
if __name__ == "__main__":
    print("=== ĐANG TEST KẾT NỐI DB ===")
    print("File này đang được chạy trực tiếp!")
    print(f"Giá trị __name__ = {__name__}")
    
    connect_db()
    data = query_data()
    print(f"Dữ liệu: {data}")
    
    print("=== KẾT THÚC TEST ===")
else:
    # File này đang được import từ file khác
    print(f"File database.py đang được import (__name__ = {__name__})")
    print("Code trong if __name__ == '__main__' sẽ KHÔNG chạy")

