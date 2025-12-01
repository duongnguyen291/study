# Ví dụ về các kiểu Import

## Mục đích
Ví dụ này minh họa 3 cách import module và ưu nhược điểm của từng cách.

## Các file

1. **calculator.py**: Module chứa các hàm tính toán
2. **test_import_module.py**: Cách 1 - Import cả module
3. **test_import_specific.py**: Cách 2 - Import cụ thể (Khuyên dùng)
4. **test_import_all.py**: Cách 3 - Import tất cả (Tối kỵ)

## Cách chạy

```bash
# Cách 1: Import cả module
python test_import_module.py

# Cách 2: Import cụ thể
python test_import_specific.py

# Cách 3: Import tất cả (xem lỗi)
python test_import_all.py
```

## So sánh

| Cách | Ưu điểm | Nhược điểm | Khi nào dùng |
|------|---------|------------|--------------|
| `import module` | Rõ ràng nguồn gốc | Code dài hơn | Module có nhiều hàm cần dùng |
| `from module import func` | Code ngắn gọn | Có thể trùng tên | Chỉ cần 1-2 hàm (Khuyên dùng) |
| `from module import *` | Tiện lợi | Nguy hiểm, dễ trùng tên | **KHÔNG NÊN DÙNG** |

## Bài học

- **Cách 2** (`from module import func`) là chuẩn mực trong Backend (Django, FastAPI)
- **Cách 3** (`import *`) rất nguy hiểm vì có thể đè lên hàm built-in của Python
- Luôn biết rõ hàm của mình đến từ đâu

