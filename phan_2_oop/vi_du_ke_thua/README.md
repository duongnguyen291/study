# Ví dụ về Kế thừa (Inheritance)

## Mục đích
Ví dụ này minh họa khái niệm Kế thừa trong OOP - "Con nhà tông, không giống lông cũng giống cánh".

## Các file

1. **ke_thua_gia_dinh.py**: Ví dụ về Bố và Con
   - Con kế thừa `an()` và `ngu()` từ Bố
   - Con có thêm phương thức riêng: `choi_game()`, `luot_tiktok()`

2. **ke_thua_dong_vat.py**: Ví dụ về Animal -> Dog, Cat
   - Dog và Cat kế thừa `chay()` và `an()` từ Animal
   - Mỗi class con ghi đè `keu()` với cách kêu riêng

## Cách chạy

```bash
# Ví dụ 1: Gia đình
python ke_thua_gia_dinh.py

# Ví dụ 2: Động vật
python ke_thua_dong_vat.py
```

## Khái niệm

### Kế thừa (Inheritance)
- Class con kế thừa tất cả thuộc tính và phương thức từ class cha
- Tránh code lặp lại
- Cú pháp: `class Con(Cha):`

### Ghi đè (Override)
- Class con có thể ghi đè phương thức của class cha
- Ví dụ: `Dog.keu()` ghi đè `Animal.keu()`

### super()
- Dùng để gọi phương thức của class cha
- Ví dụ: `super().__init__(ten)` gọi constructor của class cha

## Ưu điểm

1. **Tránh code lặp lại**: Viết code một lần, dùng nhiều nơi
2. **Dễ bảo trì**: Sửa class cha, tất cả class con tự động cập nhật
3. **Mở rộng dễ dàng**: Thêm class con mới mà không cần viết lại code cũ

## Bài học

1. **Kế thừa giúp lười biếng thông minh**: Không cần viết lại code đã có
2. **Class con có thể mở rộng**: Thêm phương thức và thuộc tính riêng
3. **Ghi đè để tùy chỉnh**: Mỗi class con có thể có hành vi riêng

## Thực hành

1. Tạo class `Bird` kế thừa từ `Animal` với phương thức `bay()`
2. Thêm class `Baby` kế thừa từ `Con` với phương thức `khoc()`
3. Thử gọi `super()` trong các phương thức của class con

