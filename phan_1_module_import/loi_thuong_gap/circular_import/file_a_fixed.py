"""
File A - Phiên bản đã sửa (Không còn Circular Import)
Giải pháp: Import file_common thay vì file_b
"""

from file_common import common_function

def function_a():
    """Hàm trong file A"""
    print("Đang chạy function_a()")
    common_function()  # Dùng hàm chung

if __name__ == "__main__":
    function_a()

