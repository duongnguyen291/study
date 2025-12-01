"""
Class TraSua - Đại diện cho một ly trà sữa
Đây là đối tượng dữ liệu (Data Object) - thành phần nhỏ nhất
"""


class TraSua:
    """
    Class đại diện cho một ly trà sữa
    """
    
    def __init__(self, ten, gia, size="M", topping="Không"):
        """
        Hàm khởi tạo
        
        Args:
            ten: Tên món trà sữa
            gia: Giá tiền (nghìn đồng)
            size: Kích cỡ (S, M, L) - Mặc định là M
            topping: Topping (mặc định là "Không")
        """
        self.ten = ten
        self.size = size
        self.topping = topping
        
        # Nếu có topping, tự động cộng thêm 5k
        if topping != "Không":
            self.gia = gia + 5
        else:
            self.gia = gia
    
    def __str__(self):
        """
        Magic method - Được gọi khi print() hoặc str()
        Giúp in ra thông tin đẹp mắt thay vì dòng code khó hiểu
        """
        topping_str = f" + {self.topping}" if self.topping != "Không" else ""
        return f"{self.ten} ({self.size}){topping_str} - {self.gia}k"
    
    def tinh_gia_chuan(self):
        """
        Tính giá chuẩn (không tính topping)
        """
        if self.topping != "Không":
            return self.gia - 5
        return self.gia

