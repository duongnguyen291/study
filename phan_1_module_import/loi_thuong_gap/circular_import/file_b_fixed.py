"""
File B - Phiên bản đã sửa (Không còn Circular Import)
Giải pháp: Import file_common thay vì file_a
"""

from file_common import common_function

def function_b():
    """Hàm trong file B"""
    print("Đang chạy function_b()")
    common_function()  # Dùng hàm chung

if __name__ == "__main__":
    function_b()

