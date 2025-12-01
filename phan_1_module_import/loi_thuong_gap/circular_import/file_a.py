"""
File A - Ví dụ về Circular Import (Import vòng tròn)
⚠️ ĐÂY LÀ VÍ DỤ LỖI - KHÔNG NÊN LÀM VẬY!
"""

# File A import File B
from file_b import function_b

def function_a():
    """Hàm trong file A"""
    print("Đang chạy function_a()")
    function_b()  # Gọi hàm từ file B

if __name__ == "__main__":
    function_a()

