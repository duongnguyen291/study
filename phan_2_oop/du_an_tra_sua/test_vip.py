"""
File test_vip.py - Test chức năng VIP
"""

from models import TraSua, HoaDonVIP


def test_hoa_don_vip():
    """Test class HoaDonVIP"""
    print("=== TEST CLASS HOADONVIP ===")
    
    # Tạo hóa đơn VIP
    bill_vip = HoaDonVIP("Khách VIP")
    
    # Tạo các món
    ts1 = TraSua("Trà sữa trân châu", 30, "L")
    ts2 = TraSua("Matcha đá xay", 50, "L")
    
    # Thêm món
    bill_vip.them_mon(ts1)  # 30k
    bill_vip.them_mon(ts2)  # 50k
    # Tổng gốc: 80k
    
    # Test tính tổng với giảm giá
    tong_vip = bill_vip.tinh_tong_tien()
    print(f"\nTổng tiền VIP (sau giảm 10%): {tong_vip}k")
    
    # Kiểm tra: 80k * 0.9 = 72k
    expected = int(80 * 0.9)
    assert tong_vip == expected, f"Lỗi! Tổng VIP phải là {expected}k, nhưng nhận được {tong_vip}k"
    
    # In hóa đơn VIP
    bill_vip.in_hoa_don()
    
    print("✅ Test HoaDonVIP thành công!\n")


if __name__ == "__main__":
    test_hoa_don_vip()
    print("🎉 Test VIP thành công!")

