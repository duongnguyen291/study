"""
✅ ĐÂY LÀ CÁCH ĐÚNG: Đặt tên file không trùng với thư viện chuẩn
File này có thể import thư viện email của Python mà không bị xung đột
"""

# Bây giờ có thể import thư viện email chuẩn của Python
import email  # ✅ Hoạt động bình thường!

from email.message import EmailMessage

# Sử dụng thư viện email chuẩn
msg = EmailMessage()
msg['From'] = 'sender@example.com'
msg['To'] = 'receiver@example.com'
msg['Subject'] = 'Test Email'
msg.set_content('Nội dung email')

print("✅ Import thư viện email thành công!")
print(f"Loại: {type(msg)}")

"""
Bài học: 
- Không đặt tên file trùng với thư viện chuẩn của Python
- Các tên cần tránh: email, json, sys, os, math, random, datetime, etc.
"""

