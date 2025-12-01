"""
Ví dụ về Đóng gói (Encapsulation)
Minh họa: Public và Private - Cái vỏ bảo vệ
"""


class TaiKhoanNganHang:
    """
    Ví dụ về Encapsulation
    Mật khẩu và số tiền phải được bảo vệ (Private)
    Chỉ cho phép truy cập qua "cửa chính" (Public method)
    """
    
    def __init__(self, so_tai_khoan, mat_khau, so_tien=0):
        # Public attribute - Ai cũng có thể xem
        self.so_tai_khoan = so_tai_khoan
        
        # Private attribute - Bắt đầu bằng __ (2 dấu gạch dưới)
        # Không nên truy cập trực tiếp từ bên ngoài
        self.__mat_khau = mat_khau
        self.__so_tien = so_tien
    
    # Public method - "Cửa chính" để truy cập dữ liệu private
    def xem_so_tien(self, mat_khau):
        """Xem số tiền - Cần mật khẩu"""
        if mat_khau == self.__mat_khau:
            return self.__so_tien
        else:
            return "Sai mật khẩu!"
    
    def nap_tien(self, so_tien, mat_khau):
        """Nạp tiền - Cần mật khẩu"""
        if mat_khau == self.__mat_khau:
            if so_tien > 0:
                self.__so_tien += so_tien
                return f"Nạp thành công! Số dư: {self.__so_tien}"
            else:
                return "Số tiền phải lớn hơn 0!"
        else:
            return "Sai mật khẩu!"
    
    def rut_tien(self, so_tien, mat_khau):
        """Rút tiền - Cần mật khẩu và kiểm tra số dư"""
        if mat_khau == self.__mat_khau:
            if so_tien > 0:
                if so_tien <= self.__so_tien:
                    self.__so_tien -= so_tien
                    return f"Rút thành công! Số dư còn lại: {self.__so_tien}"
                else:
                    return "Số dư không đủ!"
            else:
                return "Số tiền phải lớn hơn 0!"
        else:
            return "Sai mật khẩu!"
    
    def doi_mat_khau(self, mat_khau_cu, mat_khau_moi):
        """Đổi mật khẩu"""
        if mat_khau_cu == self.__mat_khau:
            self.__mat_khau = mat_khau_moi
            return "Đổi mật khẩu thành công!"
        else:
            return "Sai mật khẩu cũ!"


# ========== SỬ DỤNG ==========

# Tạo tài khoản
tai_khoan = TaiKhoanNganHang("123456", "abc123", 1000)

print("=== THÔNG TIN TÀI KHOẢN ===")
print(f"Số tài khoản: {tai_khoan.so_tai_khoan}")  # ✅ Public - Có thể xem

# ❌ KHÔNG NÊN truy cập trực tiếp private attribute
# print(tai_khoan.__mat_khau)  # Lỗi hoặc không hoạt động đúng
# print(tai_khoan.__so_tien)  # Lỗi hoặc không hoạt động đúng

print("\n=== XEM SỐ TIỀN ===")
# ✅ Đúng cách: Dùng method công khai
print(f"Số tiền (sai mật khẩu): {tai_khoan.xem_so_tien('sai')}")
print(f"Số tiền (đúng mật khẩu): {tai_khoan.xem_so_tien('abc123')}")

print("\n=== NẠP TIỀN ===")
print(tai_khoan.nap_tien(500, "abc123"))
print(f"Số dư sau nạp: {tai_khoan.xem_so_tien('abc123')}")

print("\n=== RÚT TIỀN ===")
print(tai_khoan.rut_tien(200, "abc123"))
print(tai_khoan.rut_tien(2000, "abc123"))  # Số dư không đủ
print(f"Số dư sau rút: {tai_khoan.xem_so_tien('abc123')}")

print("\n=== ĐỔI MẬT KHẨU ===")
print(tai_khoan.doi_mat_khau("abc123", "xyz789"))
print(f"Số tiền (mật khẩu mới): {tai_khoan.xem_so_tien('xyz789')}")

"""
Quan sát:
- Mật khẩu và số tiền được bảo vệ (private) - Không thể truy cập trực tiếp
- Chỉ có thể truy cập qua "cửa chính" (public method) với mật khẩu đúng
- Đây là Encapsulation: Bảo vệ dữ liệu quan trọng
"""

