"""
Cách 3: Import tất cả (Tối kỵ - Anti Pattern)
⚠️ KHÔNG NÊN DÙNG!
"""

from calculator import *

# Có vẻ tiện lợi, nhưng nguy hiểm!
ket_qua = add(5, 3)
print(f"5 + 3 = {ket_qua}")

# ⚠️ VẤN ĐỀ: Hàm open() của calculator đã đè lên hàm open() của Python!
# Bây giờ bạn không thể dùng hàm open() chuẩn của Python nữa!


try:
    # Thử mở file bằng hàm open() của Python
    with open("test.txt", "w") as f:
        f.write("Hello")
    print("Mở file thành công")
except Exception as e:
    print(f"Lỗi: {e}")

# Hàm open() của calculator đã thay thế hàm open() của Python!
# Đây là lý do tại sao KHÔNG NÊN dùng import *

