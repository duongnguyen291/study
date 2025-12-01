"""
File B - Ví dụ về Circular Import (Import vòng tròn)
⚠️ ĐÂY LÀ VÍ DỤ LỖI - KHÔNG NÊN LÀM VẬY!
"""

# File B import File A -> TẠO RA VÒNG TRÒN!
from file_a import function_a

def function_b():
    """Hàm trong file B"""
    print("Đang chạy function_b()")
    function_a()  # Gọi hàm từ file A

if __name__ == "__main__":
    function_b()

"""
Khi chạy file_a.py hoặc file_b.py, Python sẽ báo lỗi:
ImportError: cannot import name 'function_a' from partially initialized module 'file_a'

Lý do: 
- file_a.py đang import file_b.py
- file_b.py đang import file_a.py
- Python không biết nên load file nào trước -> Lỗi!
"""

