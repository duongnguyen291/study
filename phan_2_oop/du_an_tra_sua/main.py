"""
File main.py - Chạy chương trình Quán Trà Sữa
Kết nối các Object lại với nhau
"""

from models import TraSua, HoaDon, HoaDonVIP, KhachHang


def main():
    """
    Hàm chính - Chạy chương trình
    """
    print("=" * 50)
    print(" " * 15 + "QUÁN TRÀ SỮA")
    print("=" * 50)
    
    # ========== BƯỚC 1: Tạo các món (Các object TraSua) ==========
    print("\n📝 Tạo các món trà sữa...")
    
    ts_tran_chau = TraSua("Trà sữa trân châu", 30, "L")
    ts_dao = TraSua("Trà đào cam sả", 45, "M")
    ts_matcha = TraSua("Matcha đá xay", 50, "L")
    ts_oreo = TraSua("Trà sữa Oreo", 40, "M", "Kem cheese")  # Có topping
    
    print(f"✅ Đã tạo: {ts_tran_chau}")
    print(f"✅ Đã tạo: {ts_dao}")
    print(f"✅ Đã tạo: {ts_matcha}")
    print(f"✅ Đã tạo: {ts_oreo}")
    
    # ========== BƯỚC 2: Tạo hóa đơn thường ==========
    print("\n" + "=" * 50)
    print("💰 HÓA ĐƠN KHÁCH HÀNG THƯỜNG")
    print("=" * 50)
    
    # Tạo một hóa đơn mới (Object HoaDon)
    bill_cua_nam = HoaDon()
    
    # Thêm món vào hóa đơn (Tương tác giữa HoaDon và TraSua)
    # Chú ý: Ta truyền cả cái object ts_tran_chau vào hàm them_mon
    bill_cua_nam.them_mon(ts_tran_chau)
    bill_cua_nam.them_mon(ts_matcha)
    
    # In kết quả
    bill_cua_nam.in_hoa_don()
    
    # ========== BƯỚC 3: Tạo hóa đơn VIP ==========
    print("=" * 50)
    print("⭐ HÓA ĐƠN KHÁCH HÀNG VIP")
    print("=" * 50)
    
    # Tạo hóa đơn VIP (Object HoaDonVIP)
    bill_vip = HoaDonVIP("Sơn Tùng MTP")
    
    # Thêm món vào hóa đơn VIP
    bill_vip.them_mon(ts_tran_chau)  # Giá 30k
    bill_vip.them_mon(ts_matcha)  # Giá 50k -> Tổng gốc 80k
    
    # In hóa đơn VIP (sẽ tự động dùng logic giảm giá)
    bill_vip.in_hoa_don()
    
    # ========== BƯỚC 4: Quản lý khách hàng ==========
    print("=" * 50)
    print("👤 QUẢN LÝ KHÁCH HÀNG")
    print("=" * 50)
    
    # Tạo khách hàng
    khach_1 = KhachHang("Nguyễn Văn A", "Thường")
    khach_2 = KhachHang("Trần Thị B", "VIP")
    
    # Khách mua hàng
    khach_1.mua_hang(80)  # Mua hóa đơn 80k
    khach_2.mua_hang(72)  # Mua hóa đơn VIP 72k
    
    print(f"Khách hàng 1: {khach_1}")
    print(f"Khách hàng 2: {khach_2}")
    
    # Nâng cấp VIP
    print("\n🎁 Nâng cấp VIP...")
    khach_1.nang_cap_vip()
    print(f"Sau nâng cấp: {khach_1}")
    
    # ========== BƯỚC 5: Demo thêm tính năng ==========
    print("\n" + "=" * 50)
    print("🔧 DEMO THÊM TÍNH NĂNG")
    print("=" * 50)
    
    # Tạo hóa đơn mới
    bill_demo = HoaDon()
    bill_demo.them_mon(ts_dao)
    bill_demo.them_mon(ts_oreo)
    bill_demo.them_mon(ts_matcha)
    
    print(f"\nSố lượng món: {bill_demo.so_luong_mon()}")
    bill_demo.in_hoa_don()
    
    # Xóa món
    print("Xóa món ở vị trí 2...")
    bill_demo.xoa_mon(2)
    bill_demo.in_hoa_don()


if __name__ == "__main__":
    main()

