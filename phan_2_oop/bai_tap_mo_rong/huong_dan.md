# Hướng dẫn mở rộng hệ thống Quán Trà Sữa

## Yêu cầu bài tập về nhà

Dựa trên hệ thống Quán Trà Sữa hiện tại, hãy mở rộng với các tính năng sau:

### 1. Thêm thuộc tính topping vào class TraSua ✅ (Đã có)

Hiện tại class `TraSua` đã có thuộc tính `topping`. Nếu có topping, giá tự động cộng thêm 5k.

### 2. Tạo class KhachHangThanThiet (giảm 5%)

Tạo class `KhachHangThanThiet` kế thừa từ `HoaDon` (hoặc tạo class riêng), với logic giảm giá 5%.

**Gợi ý:**
```python
class HoaDonThanThiet(HoaDon):
    def __init__(self, ten_khach):
        super().__init__()
        self.ten_khach = ten_khach
    
    def tinh_tong_tien(self):
        tong_goc = super().tinh_tong_tien()
        return int(tong_goc * 0.95)  # Giảm 5%
```

### 3. Mở rộng thêm (Nâng cao)

#### a. Thêm class NhanVien
- Thuộc tính: `ten`, `ma_nhan_vien`, `luong`
- Phương thức: `ban_hang()`, `tinh_luong()`

#### b. Thêm class QuanLy
- Kế thừa từ `NhanVien`
- Thêm phương thức: `xem_doanh_thu()`, `xem_hoa_don()`

#### c. Thêm tính năng vào HoaDon
- `them_giam_gia()`: Thêm mã giảm giá
- `tinh_phu_phi()`: Tính phí phục vụ (5% nếu hóa đơn > 100k)

#### d. Thêm class Menu
- Quản lý danh sách các món trà sữa
- Phương thức: `them_mon()`, `xoa_mon()`, `tim_mon()`, `hien_thi_menu()`

## Cấu trúc đề xuất

```
models/
├── tra_sua.py
├── hoa_don.py
├── hoa_don_vip.py
├── hoa_don_than_thiet.py  # Mới
├── khach_hang.py
├── nhan_vien.py           # Mới (nâng cao)
├── quan_ly.py             # Mới (nâng cao)
└── menu.py                # Mới (nâng cao)
```

## Hướng dẫn làm bài

1. **Đọc kỹ code hiện tại**: Hiểu cách các class tương tác với nhau
2. **Tạo class mới**: Dựa trên mẫu `HoaDonVIP`, tạo `HoaDonThanThiet`
3. **Test kỹ**: Tạo file `test_than_thiet.py` để test
4. **Mở rộng từng bước**: Không làm tất cả cùng lúc, làm từng phần một

## Tiêu chí chấm điểm

- ✅ Code chạy được, không lỗi
- ✅ Sử dụng đúng kế thừa
- ✅ Logic tính tiền đúng (giảm 5%)
- ✅ Code có comment rõ ràng
- ✅ Có file test

## File giải mẫu

Xem thư mục `giai_mau/` để tham khảo code mẫu (nếu cần).

