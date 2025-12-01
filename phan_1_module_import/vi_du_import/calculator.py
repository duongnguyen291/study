"""
Module Calculator - Ví dụ về các kiểu import
File này chứa các hàm tính toán cơ bản
"""

def add(a, b):
    """Cộng hai số"""
    return a + b


def sub(a, b):
    """Trừ hai số"""
    return a - b


def mul(a, b):
    """Nhân hai số"""
    return a * b


def div(a, b):
    """Chia hai số: a/b. Raise"""
    if b == 0:
        raise ValueError("Không thể chia cho 0!")
    return a / b


# ⚠️ CẢNH BÁO: Hàm này trùng tên với hàm built-in của Python
def open(filename):
    """Hàm này trùng tên với hàm open() của Python - KHÔNG NÊN LÀM VẬY!"""
    print(f"Đang mở file: {filename}")
    return f"File {filename} đã mở"
