"""
Ví dụ cơ bản về Class và Object
Minh họa: Class là khuôn, Object là sản phẩm
"""

# Bản vẽ robot --> Ra thành các con robot thực sự. 
class Robot:
    """
    Class Robot - Đây là "khuôn" để tạo ra các con Robot
    Class chỉ là bản vẽ thiết kế, không phải Robot thật
    """
    
    def __init__(self, ten, mau_sac, chieu_cao, toc_he):
        """
        Hàm khởi tạo (Constructor)
        Được gọi tự động khi tạo object mới
        """
        # Đây là THUỘC TÍNH (Attribute)
        self.ten = ten
        self.mau_sac = mau_sac
        self.chieu_cao = chieu_cao
        self.toc_he = toc_he
        self.nang_luong = 100  # Năng lượng mặc định

    def chay(self):
        """Phương thức (Method) - Hành động của Robot"""
        if self.nang_luong > 0:
            self.nang_luong = self.nang_luong - 10
            print(f"{self.ten} đang chạy! Năng lượng còn: {self.nang_luong}")
        else:
            print(f"{self.ten} hết năng lượng, không thể chạy!")
    
    def nap_dien(self):
        """Phương thức nạp điện"""
        self.nang_luong = 100
        print(f"{self.ten} đã được nạp đầy năng lượng!")


# ========== SỬ DỤNG ==========

# Tạo các Object (Robot thật) từ Class Robot (khuôn)
robot_a = Robot("Robot A", "Xanh","2m","co dien")
robot_b = Robot("Robot B", "Đỏ","10m","khong lo")

print("=== Robot A ===")
print(f"Tên: {robot_a.ten}")
print(f"Màu: {robot_a.mau_sac}")
print(f"Năng lượng: {robot_a.nang_luong}")

print("\n=== Robot B ===")
print(f"Tên: {robot_b.ten}")
print(f"Màu: {robot_b.mau_sac}")

# Gọi phương thức
print("\n=== Robot A chạy ===")
robot_a.chay()
robot_a.chay()
robot_a.chay()

print("\n=== Robot B chạy ===")
robot_b.chay()

print("\n=== Nạp điện cho Robot A ===")
robot_a.nap_dien()
robot_a.chay()

"""
Quan sát:
- Từ 1 Class Robot, ta có thể tạo nhiều Object (robot_a, robot_b)
- Mỗi Object có thuộc tính riêng (ten, mau_sac, nang_luong)
- Mỗi Object có thể thực hiện các phương thức (chay, nap_dien)
"""

