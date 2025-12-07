"""
Ví dụ về Class nhân vật Game
Minh họa: Thuộc tính (Attribute) và Phương thức (Method)
"""


class NhanVatGame:
    """
    Class đại diện cho nhân vật trong game
    """
    
    def __init__(self, ten, mau_sac):
        """
        Hàm khởi tạo
        Đây là THUỘC TÍNH (Đặc điểm) - Nó trông như thế nào?
        """
        self.ten = ten  # Tên: Yasuo, Steve...
        self.mau_sac = mau_sac  # Màu: Xanh, Đỏ...
        self.hp = 100  # Máu mặc định là 100
        self.mana = 50  # Năng lượng phép thuật
    
    def chay(self):
        """
        Đây là PHƯƠNG THỨC (Hành động) - Nó làm được gì?
        """
        print(f"{self.ten} đang chạy rất nhanh!")
    
    def bi_danh(self, sat_thuong=10):
        """
        Phương thức bị đánh - giảm máu
        """
        self.hp = self.hp - sat_thuong
        if self.hp <= 0:
            print(f"Á á! {self.ten} đã chết! (HP: 0)")
        else:
            print(f"Á á! {self.ten} bị đánh. Máu còn: {self.hp}")
    
    def hoi_mau(self, so_mau=20):
        """
        Phương thức hồi máu
        """
        self.hp = min(100, self.hp + so_mau)  # Không vượt quá 100
        print(f"{self.ten} đã hồi máu! HP hiện tại: {self.hp}")
    
    def xem_thong_tin(self):
        """
        Phương thức xem thông tin nhân vật
        """
        print(f"=== THÔNG TIN NHÂN VẬT ===")
        print(f"Tên: {self.ten}")
        print(f"Màu: {self.mau_sac}")
        print(f"HP: {self.hp}/100")
        print(f"Mana: {self.mana}/50")


# ========== SỬ DỤNG ==========

# Tạo nhân vật
yasuo = NhanVatGame("Yasuo", "Xanh") # khởi tạo đối tượng
steve = NhanVatGame("Steve", "Nâu") # khởi tạo đối tượng

print("=== YASUO ===")
yasuo.xem_thong_tin()
yasuo.chay()
yasuo.bi_danh(15)
yasuo.bi_danh(20)
yasuo.hoi_mau(30)
yasuo.xem_thong_tin()

print("\n=== STEVE ===")
steve.xem_thong_tin()
steve.chay()
steve.bi_danh(50)
steve.hoi_mau()

"""
Quan sát:
- Mỗi nhân vật có thuộc tính riêng (ten, mau_sac, hp, mana)
- Mỗi nhân vật có thể thực hiện các hành động (chay, bi_danh, hoi_mau)
- Thuộc tính thay đổi khi thực hiện hành động (hp giảm khi bị đánh, tăng khi hồi máu)
"""

