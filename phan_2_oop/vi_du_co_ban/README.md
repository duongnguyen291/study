# Ví dụ cơ bản về Class và Object

## Mục đích
Ví dụ này minh họa các khái niệm cơ bản của OOP: Class, Object, Attribute, Method.

## Các file

1. **class_object.py**: Ví dụ về Class Robot và Object
   - Class là "khuôn", Object là "sản phẩm"
   - Từ 1 Class có thể tạo nhiều Object

2. **nhan_vat_game.py**: Ví dụ về nhân vật game
   - Thuộc tính (Attribute): ten, mau_sac, hp, mana
   - Phương thức (Method): chay(), bi_danh(), hoi_mau()

## Cách chạy

```bash
# Ví dụ 1: Class và Object
python class_object.py

# Ví dụ 2: Nhân vật game
python nhan_vat_game.py
```

## Khái niệm

### Class (Lớp)
- Là "khuôn mẫu" để tạo ra các object
- Chỉ là bản vẽ thiết kế, không phải object thật
- Ví dụ: `class Robot:` là khuôn để tạo robot

### Object (Đối tượng)
- Là "sản phẩm" được tạo ra từ class
- Có thật, có thể sử dụng
- Ví dụ: `robot_a = Robot()` là robot thật

### Attribute (Thuộc tính)
- Mô tả đặc điểm của object
- Ví dụ: `ten`, `mau_sac`, `hp`, `nang_luong`

### Method (Phương thức)
- Mô tả hành động của object
- Ví dụ: `chay()`, `bi_danh()`, `hoi_mau()`

## Bài học

1. **Class là khuôn, Object là sản phẩm**: Từ 1 class có thể tạo nhiều object
2. **Mỗi object độc lập**: Object này thay đổi không ảnh hưởng object khác
3. **Attribute và Method**: Object có đặc điểm (attribute) và hành động (method)

## Thực hành

1. Tạo thêm một object Robot mới với tên và màu khác
2. Thử thay đổi thuộc tính của một object và quan sát
3. Thêm phương thức mới cho class NhanVatGame (ví dụ: `tan_cong()`)

