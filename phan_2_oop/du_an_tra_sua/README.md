# Dự án: Quán Trà Sữa (Milk Tea POS System)

## Mục đích
Dự án tổng hợp áp dụng toàn bộ kiến thức OOP đã học: Class, Object, Inheritance, Encapsulation.

## Cấu trúc

```
du_an_tra_sua/
├── models/
│   ├── __init__.py
│   ├── tra_sua.py          # Class TraSua - Đại diện cho ly trà sữa
│   ├── hoa_don.py          # Class HoaDon - Quản lý hóa đơn
│   ├── hoa_don_vip.py      # Class HoaDonVIP - Hóa đơn VIP (kế thừa)
│   └── khach_hang.py       # Class KhachHang - Quản lý khách hàng
├── main.py                 # File chạy chính
├── test_basic.py           # Test chức năng cơ bản
├── test_vip.py            # Test chức năng VIP
└── README.md              # File này
```

## Cách chạy

### Chạy chương trình chính
```bash
cd du_an_tra_sua
python main.py
```

### Chạy test
```bash
# Test chức năng cơ bản
python test_basic.py

# Test chức năng VIP
python test_vip.py
```

## Các Class

### 1. TraSua (Đối tượng dữ liệu)
- **Thuộc tính**: `ten`, `gia`, `size`, `topping`
- **Phương thức**: `__str__()`, `tinh_gia_chuan()`
- **Đặc điểm**: Tự động cộng thêm 5k nếu có topping

### 2. HoaDon (Đối tượng quản lý)
- **Thuộc tính**: `danh_sach_mon` (List chứa các object TraSua)
- **Phương thức**: 
  - `them_mon()`: Thêm món vào hóa đơn
  - `tinh_tong_tien()`: Tính tổng tiền
  - `in_hoa_don()`: In hóa đơn
  - `xoa_mon()`: Xóa món
  - `so_luong_mon()`: Đếm số lượng món

### 3. HoaDonVIP (Kế thừa từ HoaDon)
- **Kế thừa**: Tất cả tính năng của HoaDon
- **Ghi đè**: `tinh_tong_tien()` - Giảm 10%
- **Ghi đè**: `in_hoa_don()` - Hiển thị thông tin VIP

### 4. KhachHang
- **Thuộc tính**: `ten`, `loai`, `so_lan_mua`, `tong_tien_da_mua`
- **Phương thức**: `mua_hang()`, `nang_cap_vip()`

## Điểm chốt

### 1. Object trong Object
```python
bill = HoaDon()
bill.danh_sach_mon.append(ts_tran_chau)  # List chứa object TraSua
```

### 2. Kế thừa và Ghi đè
```python
class HoaDonVIP(HoaDon):  # Kế thừa
    def tinh_tong_tien(self):  # Ghi đè
        tong_goc = super().tinh_tong_tien()  # Gọi phương thức cha
        return tong_goc * 0.9  # Giảm 10%
```

### 3. Magic Method
```python
def __str__(self):
    return f"{self.ten} ({self.size}) - {self.gia}k"
# Khi print(ts), Python tự động gọi __str__()
```

## Bài học

1. **Chia nhỏ vấn đề**: TraSua là đơn vị nhỏ nhất, HoaDon quản lý nhiều TraSua
2. **Kế thừa tránh lặp code**: HoaDonVIP kế thừa HoaDon, chỉ cần ghi đè logic tính tiền
3. **Dễ bảo trì**: Sửa TraSua chỉ ảnh hưởng TraSua, không ảnh hưởng HoaDon

## Mở rộng

Xem thư mục `bai_tap_mo_rong/` để có hướng dẫn mở rộng hệ thống.

