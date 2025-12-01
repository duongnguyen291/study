"""
Ví dụ về Module cơ bản - File lib.py
File này minh họa cách Python thực thi code khi import
"""


def hello():
    """Hàm hello - chỉ chạy khi được gọi"""
    print("Xin chào")


def tinh_tong(a, b):
    """Hàm tính tổng hai số"""
    return a + b

if __name__ == "__main__":
    print("Đây là dòng code thực thi - sẽ chạy khi chạy trực tiếp file này!")

