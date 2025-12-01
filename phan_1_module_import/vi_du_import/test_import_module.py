"""
Cách 1: Import cả module
Ưu điểm: Rõ ràng nguồn gốc, biết hàm đến từ đâu
"""

import calculator
import ghi_diem 
# Sử dụng với tên module đầy đủ
ket_qua = calculator.add(5, 3)
print(f"5 + 3 = {ket_qua}")

# ket_qua = ghi_diem.add(3,5)
ket_qua = calculator.sub(10, 4)
print(f"10 - 4 = {ket_qua}")

# Ưu điểm: Rõ ràng hàm add() đến từ calculator, không phải từ module khác

