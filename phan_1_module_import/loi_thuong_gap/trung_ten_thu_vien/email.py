"""
⚠️ CẢNH BÁO: Đây là ví dụ về lỗi đặt tên file trùng với thư viện chuẩn
KHÔNG NÊN ĐẶT TÊN FILE LÀ email.py!
"""

# Học sinh muốn import thư viện email của Python
# Nhưng Python sẽ import chính file này thay vì thư viện chuẩn!
import email  # ❌ LỖI! Python sẽ import chính file email.py này!

# Khi chạy sẽ báo lỗi vì file này không có các hàm của thư viện email chuẩn
try:
    # Thử dùng hàm của thư viện email chuẩn
    msg = email.message.EmailMessage()
    print("Thành công")
except AttributeError as e:
    print(f"❌ Lỗi: {e}")
    print("Python đã import chính file email.py này thay vì thư viện chuẩn!")

"""
Giải pháp: Đổi tên file thành:
- my_email.py
- email_utils.py
- email_helper.py
- send_email.py
"""

