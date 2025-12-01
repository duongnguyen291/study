"""
File __init__.py - "Lễ tân" của package features
File này quyết định ai ở bên ngoài được gặp ai ở bên trong
"""

# Gom các hàm quan trọng từ các file con ra "cửa chính"
from .authencation import login, logout
from .user import get_profile, update_profile

# Có thể export thêm các biến hoặc class
__all__ = ['login', 'logout', 'get_profile', 'update_profile']
# Giải thích:
# - Dấu chấm (.) trước tên module nghĩa là import từ cùng package
# - Từ bên ngoài, chỉ cần: from features import login
# - Không cần biết bên trong có file auth.py hay user.py

