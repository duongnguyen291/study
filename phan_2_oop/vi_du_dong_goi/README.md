# Ví dụ về Đóng gói (Encapsulation)

## Mục đích
Ví dụ này minh họa khái niệm Đóng gói trong OOP - Bảo vệ dữ liệu quan trọng.

## File

**encapsulation.py**: Ví dụ về tài khoản ngân hàng
- Mật khẩu và số tiền là **Private** (bắt đầu bằng `__`)
- Chỉ có thể truy cập qua **Public method** với mật khẩu đúng

## Cách chạy

```bash
python encapsulation.py
```

## Khái niệm

### Public (Công khai)
- Ai cũng có thể truy cập
- Ví dụ: `self.so_tai_khoan` (không có `__`)

### Private (Riêng tư)
- Bắt đầu bằng `__` (2 dấu gạch dưới)
- Không nên truy cập trực tiếp từ bên ngoài
- Ví dụ: `self.__mat_khau`, `self.__so_tien`

### "Cửa chính" (Public Method)
- Method công khai để truy cập dữ liệu private
- Có thể kiểm tra quyền truy cập (ví dụ: mật khẩu)
- Ví dụ: `xem_so_tien()`, `nap_tien()`, `rut_tien()`

## Tại sao cần Encapsulation?

1. **Bảo vệ dữ liệu**: Không cho phép sửa đổi trực tiếp
2. **Kiểm soát truy cập**: Chỉ cho phép truy cập qua "cửa chính"
3. **Dễ bảo trì**: Thay đổi logic ở một chỗ (trong method)

## Ví dụ thực tế

Giống như điện thoại:
- **Public**: Màn hình, nút bấm - Ai cũng có thể dùng
- **Private**: Mạch điện, pin - Được bảo vệ bên trong vỏ

## Bài học

1. **Dữ liệu quan trọng nên là Private**: Mật khẩu, số tiền, thông tin nhạy cảm
2. **Truy cập qua Public Method**: Kiểm soát cách truy cập và sửa đổi
3. **Bảo vệ khỏi lỗi**: Không cho phép sửa đổi trực tiếp, tránh lỗi

## Thực hành

1. Thử truy cập trực tiếp `tai_khoan.__so_tien` và quan sát
2. Thêm method `chuyen_tien()` để chuyển tiền giữa 2 tài khoản
3. Thêm validation: Số tiền không được âm, mật khẩu phải có ít nhất 6 ký tự

