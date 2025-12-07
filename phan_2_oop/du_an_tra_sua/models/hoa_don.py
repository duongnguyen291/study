"""
Class HoaDon - Quản lý hóa đơn
Đây là đối tượng quản lý (Manager Object) - Quan trọng!
"""

     
class HoaDon:
    """
    Class quản lý hóa đơn
    Chứa một danh sách các ly trà sữa (Object trong Object)
    """
    def __init__(self):
        """
        Hàm khởi tạo
        Thuộc tính này là một LIST rỗng để chứa các object TraSua
        """
        self.danh_sach_mon = []  # List chứa các object TraSua
    
    def them_mon(self, mon):
        """
        Phương thức thêm món vào list
        
        Args:
            mon: Một object TraSua
        """
        # 'mon' ở đây sẽ là một Object TraSua
        self.danh_sach_mon.append(mon)
        print(f"✅ Đã thêm: {mon.ten}")
    
    def tinh_tong_tien(self):
        """
        Phương thức tính tổng tiền (Logic nghiệp vụ)
        
        Returns:
            Tổng tiền của tất cả món trong hóa đơn
        """
        tong = 0
        for mon in self.danh_sach_mon:
            tong += mon.gia  # Cộng dồn giá của từng món
        return tong
    
    def in_hoa_don(self):
        """
        Phương thức in hóa đơn
        """
        print("\n" + "=" * 40)
        print(" " * 10 + "HÓA ĐƠN")
        print("=" * 40)
        
        if len(self.danh_sach_mon) == 0:
            print("Hóa đơn trống!")
            return
        
        # In từng món
        for i, mon in enumerate(self.danh_sach_mon, 1):
            print(f"{i}. {mon}")  # Nó sẽ gọi hàm __str__ bên TraSua
        
        print("-" * 40)
        print(f"{'TỔNG CỘNG:':<30} {self.tinh_tong_tien()}k")
        print("=" * 40 + "\n")
    
    def xoa_mon(self, vi_tri):
        """
        Xóa món khỏi hóa đơn (theo vị trí)
        
        Args:
            vi_tri: Vị trí món trong danh sách (bắt đầu từ 1)
        """
        if 1 <= vi_tri <= len(self.danh_sach_mon):
            mon_bi_xoa = self.danh_sach_mon.pop(vi_tri - 1)
            print(f"✅ Đã xóa: {mon_bi_xoa.ten}")
        else:
            print("❌ Vị trí không hợp lệ!")
    
    def so_luong_mon(self):
        """
        Đếm số lượng món trong hóa đơn
        """
        return len(self.danh_sach_mon)

