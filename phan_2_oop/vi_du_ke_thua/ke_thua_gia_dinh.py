"""
Ví dụ về Kế thừa (Inheritance) - Gia đình
Minh họa: "Con nhà tông, không giống lông cũng giống cánh"
"""


class Bo:
    """
    Class Cha - Bố
    Bố biết ăn và ngủ
    """
    
    def __init__(self, ten):
        self.ten = ten
    
    def an(self):
        print(f"{self.ten} đang ăn cơm")
    
    def ngu(self):
        print(f"{self.ten} đang ngủ")


class Con(Bo):
    """
    Class Con - Kế thừa từ class Bo
    Con sinh ra đã biết ăn và ngủ giống bố (không cần học lại)
    Nhưng con còn biết thêm chơi game và lướt TikTok
    """
    
    def __init__(self, ten, tuoi):
        # Gọi hàm khởi tạo của class cha
        super().__init__(ten)
        self.tuoi = tuoi  # Thuộc tính riêng của Con
    
    # Con kế thừa an() và ngu() từ Bo, không cần viết lại
    
    def choi_game(self):
        """Phương thức riêng của Con - Bố không biết"""
        print(f"{self.ten} đang chơi game")
    
    def luot_tiktok(self):
        """Phương thức riêng của Con - Bố không biết"""
        print(f"{self.ten} đang lướt TikTok")


# ========== SỬ DỤNG ==========

print("=== BỐ ===")
bo = Bo("Bố Nam")
bo.an()
bo.ngu()
# bo.choi_game()  # ❌ Lỗi! Bố không biết chơi game

print("\n=== CON ===")
con = Con("Con An", 15)
con.an()  # ✅ Kế thừa từ Bố
con.ngu()  # ✅ Kế thừa từ Bố
con.choi_game()  # ✅ Phương thức riêng của Con
con.luot_tiktok()  # ✅ Phương thức riêng của Con

print(f"\nCon có tuổi: {con.tuoi}")  # Thuộc tính riêng của Con

"""
Quan sát:
- Con kế thừa an() và ngu() từ Bo, không cần viết lại code
- Con có thêm phương thức riêng: choi_game(), luot_tiktok()
- Con có thuộc tính riêng: tuoi
- Đây là sức mạnh của Kế thừa: Tránh code lặp lại!
"""

