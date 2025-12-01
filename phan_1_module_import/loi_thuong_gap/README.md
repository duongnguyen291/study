# Lỗi thường gặp khi làm việc với Module và Import

## Mục đích
Thư mục này chứa các ví dụ về lỗi thường gặp và cách khắc phục.

## Các lỗi

### 1. Circular Import (Import vòng tròn)
- **Vấn đề**: File A import File B, File B import File A
- **Giải pháp**: Tách phần chung ra file riêng
- **Xem**: `circular_import/`

### 2. Đặt tên file trùng thư viện chuẩn
- **Vấn đề**: Đặt tên file là `email.py`, `json.py`, etc.
- **Giải pháp**: Đổi tên file (ví dụ: `email_utils.py`)
- **Xem**: `trung_ten_thu_vien/`

## Bài học

1. Luôn kiểm tra mối quan hệ import giữa các file
2. Tránh đặt tên file trùng với thư viện chuẩn
3. Thiết kế kiến trúc tốt để tránh circular import

