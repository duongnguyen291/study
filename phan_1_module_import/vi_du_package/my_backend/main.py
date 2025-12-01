"""
File main.py - Sử dụng package features
"""

# Cách 1: Import trực tiếp từ package (nhờ __init__.py)
from features import login, logout, get_profile

print("=== CÁCH 1: Import từ package ===")
user_info = login("admin", "password123")
print(f"Thông tin user: {user_info}")

profile = get_profile(1)
print(f"Profile: {profile}")

logout(1)

# print("\n=== CÁCH 2: Import trực tiếp từ module (không khuyên dùng) ===")
# # Cách này vẫn hoạt động nhưng không che giấu cấu trúc bên trong
# from features.auth import login as login_direct
# from features.user import get_profile as get_profile_direct

# user_info2 = login_direct("user2", "pass456")
# print(f"Thông tin user: {user_info2}")

"""
Ưu điểm của cách 1:
- Che giấu cấu trúc phức tạp bên trong package
- Nếu sau này đổi tên file auth.py -> authentication.py, chỉ cần sửa __init__.py
- Code ở main.py không cần thay đổi
"""

