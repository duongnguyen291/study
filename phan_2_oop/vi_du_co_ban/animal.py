class Animal:
    def __init__(self, name):
        self.name = name
    
    def an(self):
        print(f"{self.name} đang ăn")
    
    def chay(self):
        print(f"{self.name} đang chạy")
    
    def keu(self):
        print(f"{self.name} kêu")

    def info(self):
        print(f"Tên: {self.name}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tạo các đối tượng
    dog = Dog("Đốc", "Golden Retriever")
    cat = Cat("Kitty", "Trắng")
    
    # Gọi phương thức từ lớp cha
    print("--- Dog ---")
    dog.an()
    dog.chay()
    dog.keu()
    dog.info()
    
    print("\n--- Cat ---")
    cat.an()
    cat.chay()
    cat.keu()
    cat.info()



