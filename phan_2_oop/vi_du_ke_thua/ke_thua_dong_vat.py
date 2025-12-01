"""
Ví dụ về Kế thừa - Động vật
Minh họa: Animal -> Dog, Cat
"""


class Animal:
    """
    Class cha - Động vật
    Tất cả động vật đều biết chạy và ăn
    """
    
    def __init__(self, ten):
        self.ten = ten
        self.tuoi = 0
    
    def chay(self):
        print(f"{self.ten} đang chạy")
    
    def an(self):
        print(f"{self.ten} đang ăn")
    
    def keu(self):
        """Phương thức này sẽ bị ghi đè (override) ở class con"""
        print(f"{self.ten} đang kêu")


class Dog(Animal):
    """
    Class con - Chó
    Kế thừa từ Animal, có thêm phương thức riêng
    """
    
    def __init__(self, ten, giong):
        super().__init__(ten)  # Gọi constructor của Animal
        self.giong = giong  # Thuộc tính riêng
    
    def keu(self):
        """Ghi đè (Override) phương thức keu() của Animal"""
        print(f"{self.ten} đang sủa: Gâu gâu!")
    
    def duoi_meo(self):
        """Phương thức riêng của Dog"""
        print(f"{self.ten} đang đuổi mèo!")


class Cat(Animal):
    """
    Class con - Mèo
    Kế thừa từ Animal, có thêm phương thức riêng
    """
    
    def __init__(self, ten, mau_long):
        super().__init__(ten)
        self.mau_long = mau_long  # Thuộc tính riêng
    
    def keu(self):
        """Ghi đè (Override) phương thức keu() của Animal"""
        print(f"{self.ten} đang kêu: Meo meo!")
    
    def bat_chuot(self):
        """Phương thức riêng của Cat"""
        print(f"{self.ten} đang bắt chuột!")


# ========== SỬ DỤNG ==========

print("=== ĐỘNG VẬT ===")
dong_vat = Animal("Động vật")
dong_vat.chay()  # ✅ Tất cả động vật đều biết chạy
dong_vat.an()
dong_vat.keu()

print("\n=== CHÓ ===")
cho = Dog("Lucky", "Golden Retriever")
cho.chay()  # ✅ Kế thừa từ Animal
cho.an()  # ✅ Kế thừa từ Animal
cho.keu()  # ✅ Ghi đè phương thức keu() - Sủa thay vì kêu
cho.duoi_meo()  # ✅ Phương thức riêng của Dog
print(f"Giống: {cho.giong}")

print("\n=== MÈO ===")
meo = Cat("Tom", "Vàng")
meo.chay()  # ✅ Kế thừa từ Animal
meo.an()  # ✅ Kế thừa từ Animal
meo.keu()  # ✅ Ghi đè phương thức keu() - Meo meo
meo.bat_chuot()  # ✅ Phương thức riêng của Cat
print(f"Màu lông: {meo.mau_long}")

"""
Quan sát:
- Dog và Cat kế thừa chay() và an() từ Animal - Không cần viết lại!
- Mỗi class con ghi đè keu() với cách kêu riêng
- Mỗi class con có phương thức riêng (duoi_meo, bat_chuot)
- Đây là sức mạnh của Kế thừa: Code một lần, dùng nhiều nơi!
"""

