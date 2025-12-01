"""
Module xử lý thông tin người dùng (User)
"""


def get_profile(user_id):
    """Lấy thông tin profile của user"""
    print(f"Đang lấy profile của user ID: {user_id}")
    return {
        "user_id": user_id,
        "name": "Nguyễn Văn A",
        "email": "a@example.com"
    }


def update_profile(user_id, data):
    """Cập nhật thông tin profile"""
    print(f"Đang cập nhật profile của user ID: {user_id}")
    print(f"Dữ liệu mới: {data}")
    return True

