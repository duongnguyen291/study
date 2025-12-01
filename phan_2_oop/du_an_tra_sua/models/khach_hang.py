"""
Class KhachHang - Đại diện cho khách hàng
"""


class KhachHang:
    """
    Class đại diện cho khách hàng
    """
    
    def __init__(self, ten, loai="Thường"):
        """
        Hàm khởi tạo
        
        Args:
            ten: Tên khách hàng
            loai: Loại khách hàng ("Thường" hoặc "VIP")
        """
        self.ten = ten
        self.loai = loai
        self.so_lan_mua = 0
        self.tong_tien_da_mua = 0
    
    def mua_hang(self, so_tien):
        """
        Cập nhật thông tin khi khách mua hàng
        
        Args:
            so_tien: Số tiền khách đã mua
        """
        self.so_lan_mua += 1
        self.tong_tien_da_mua += so_tien
    
    def nang_cap_vip(self):
        """
        Nâng cấp khách hàng lên VIP
        """
        if self.loai != "VIP":
            self.loai = "VIP"
            print(f"🎉 Chúc mừng {self.ten} đã được nâng cấp lên VIP!")
        else:
            print(f"{self.ten} đã là VIP rồi!")
    
    def __str__(self):
        """
        In thông tin khách hàng
        """
        return f"{self.ten} ({self.loai}) - Đã mua {self.so_lan_mua} lần - Tổng: {self.tong_tien_da_mua}k"

