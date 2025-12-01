"""
Cách 2: Import cụ thể (Explicit Import)
Ưu điểm: Code ngắn gọn, dễ đọc
Khuyên dùng: Khi chỉ cần 1-2 hàm
"""

from calculator import add, sub, mul
# Sử dụng trực tiếp không cần tên module

ket_qua = add(5, 3)
print(f"5 + 3 = {ket_qua}")

ket_qua = sub(10, 4)
print(f"10 - 4 = {ket_qua}")

ket_qua = mul(10, 4)
print(f"10 x 4 = {ket_qua}")


# Ưu điểm: Code ngắn gọn, dễ đọc
# Đây là chuẩn mực của các framework như Django/FastAPI

