"""
Module xử lý xác thực (Authentication)
"""


def login(username, password):
    """Hàm đăng nhập"""
    print(f"Đang đăng nhập với username: {username}")
    # Logic đăng nhập ở đây
    return {"user_id": 1, "username": username, "token": "abc123"}


def logout(user_id):
    """Hàm đăng xuất"""
    print(f"Đang đăng xuất user ID: {user_id}")
    return True

