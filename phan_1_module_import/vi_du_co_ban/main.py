"""
Ví dụ về Import Module - File main.py
File này minh họa cách import và sử dụng module khác
"""

# Ngay dòng này, dòng print bên lib.py đã chạy!
import lib  # Python sẽ thực thi toàn bộ file lib.py

print("Bắt đầu chương trình chính")

# Bây giờ mới gọi hàm
lib.hello()
ket_qua = lib.tinh_tong(5, 3)
print(f"Tổng của 5 và 3 là: {ket_qua}")

"""
Kết quả khi chạy main.py:
Dòng này đang được in ra từ lib.py
Bắt đầu chương trình chính
Xin chào
Tổng của 5 và 3 là: 8
"""

