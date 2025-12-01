"""
File test_basic.py - Test các chức năng cơ bản
"""

from models import TraSua, HoaDon


def test_tra_sua():
    """Test class TraSua"""
    print("=== TEST CLASS TRASUA ===")
    
    # Test tạo trà sữa
    ts1 = TraSua("Trà sữa trân châu", 30, "L")
    print(f"Trà sữa 1: {ts1}")
    print(f"Giá: {ts1.gia}k")
    
    # Test trà sữa có topping
    ts2 = TraSua("Trà sữa Oreo", 40, "M", "Kem cheese")
    print(f"\nTrà sữa 2: {ts2}")
    print(f"Giá (có topping): {ts2.gia}k")
    print(f"Giá chuẩn (không topping): {ts2.tinh_gia_chuan()}k")
    
    print("\n✅ Test TraSua thành công!\n")


def test_hoa_don():
    """Test class HoaDon"""
    print("=== TEST CLASS HOADON ===")
    
    # Tạo hóa đơn
    bill = HoaDon()
    
    # Tạo các món
    ts1 = TraSua("Trà sữa trân châu", 30, "L")
    ts2 = TraSua("Trà đào cam sả", 45, "M")
    ts3 = TraSua("Matcha đá xay", 50, "L")
    
    # Thêm món
    bill.them_mon(ts1)
    bill.them_mon(ts2)
    bill.them_mon(ts3)
    
    # Test tính tổng
    tong = bill.tinh_tong_tien()
    print(f"\nTổng tiền: {tong}k")
    assert tong == 125, f"Lỗi! Tổng phải là 125k, nhưng nhận được {tong}k"
    
    # Test số lượng
    so_luong = bill.so_luong_mon()
    print(f"Số lượng món: {so_luong}")
    assert so_luong == 3, f"Lỗi! Số lượng phải là 3, nhưng nhận được {so_luong}"
    
    # In hóa đơn
    bill.in_hoa_don()
    
    print("✅ Test HoaDon thành công!\n")


if __name__ == "__main__":
    test_tra_sua()
    test_hoa_don()
    print("🎉 Tất cả test đều pass!")

