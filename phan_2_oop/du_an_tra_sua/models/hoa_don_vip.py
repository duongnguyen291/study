"""
Class HoaDonVIP - Hóa đơn cho khách VIP
Kế thừa từ HoaDon, ghi đè logic tính tiền để giảm giá
"""

from .hoa_don import HoaDon


class HoaDonVIP(HoaDon):
    """
    Class HoaDonVIP - Kế thừa toàn bộ tính năng của HoaDon thường
    Khách VIP được giảm 10%
    """
    
    def __init__(self, ten_khach):
        """
        Hàm khởi tạo
        Args:
            ten_khach: Tên khách hàng VIP
        """
        super().__init__()  # Gọi hàm khởi tạo của cha để có list rỗng
        self.ten_khach = ten_khach
    
    def tinh_tong_tien(self):
        """
        Ghi đè (Override) hàm tính tổng tiền
        Giảm 10% cho khách VIP
        """
        tong_goc = super().tinh_tong_tien()  # Nhờ cha tính hộ tổng gốc
        tong_giam_gia = tong_goc * 0.9  # Giảm 10%
        return int(tong_giam_gia)  # Làm tròn xuống
    
    def in_hoa_don(self):
        """
        Ghi đè hàm in hóa đơn để hiển thị thông tin VIP
        """
        print("\n" + "=" * 40)
        print(" " * 8 + "HÓA ĐƠN VIP")
        print("=" * 40)
        print(f"Khách hàng: {self.ten_khach} ⭐")
        
        if len(self.danh_sach_mon) == 0:
            print("Hóa đơn trống!")
            return
        
        # In từng món
        for i, mon in enumerate(self.danh_sach_mon, 1):
            print(f"{i}. {mon}")
        
        # Tính tổng
        tong_goc = super().tinh_tong_tien()  # Tổng gốc
        tong_giam_gia = self.tinh_tong_tien()  # Tổng sau giảm giá
        
        print("-" * 40)
        print(f"{'Tổng gốc:':<30} {tong_goc}k")
        print(f"{'Giảm giá (10%):':<30} -{tong_goc - tong_giam_gia}k")
        print(f"{'TỔNG CỘNG:':<30} {tong_giam_gia}k")
        print("=" * 40 + "\n")

