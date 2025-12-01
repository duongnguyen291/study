# Bài tập thực hành - PHẦN 1: Module và Import

## Bài tập 1: Tạo Module Calculator

### Yêu cầu:
1. Tạo file `calculator.py` với các hàm:
   - `add(a, b)`: Cộng hai số
   - `sub(a, b)`: Trừ hai số
   - `mul(a, b)`: Nhân hai số
   - `div(a, b)`: Chia hai số (xử lý chia cho 0)

2. Tạo file `test_calculator.py` để test các hàm trên bằng cách:
   - Import cả module: `import calculator`
   - Import cụ thể: `from calculator import add, sub`

3. **Không được** có code thực thi (như `print`) trôi nổi trong `calculator.py`

## Bài tập 2: Sử dụng `if __name__ == "__main__":`

### Yêu cầu:
1. Tạo file `utils.py` với các hàm:
   - `format_currency(amount)`: Định dạng số tiền (ví dụ: 100000 -> "100,000 VNĐ")
   - `validate_email(email)`: Kiểm tra email hợp lệ

2. Thêm code test trong `if __name__ == "__main__":` để test các hàm

3. Tạo file `main.py` import và sử dụng các hàm từ `utils.py`

4. **Yêu cầu**: Khi chạy `main.py`, code test trong `utils.py` không được chạy

## Bài tập 3: Tạo Package

### Yêu cầu:
Tạo cấu trúc package như sau:
```
my_project/
├── main.py
└── helpers/
    ├── __init__.py
    ├── string_utils.py    # Chứa hàm: capitalize_words(), reverse_string()
    └── number_utils.py    # Chứa hàm: is_prime(), factorial()
```

1. Trong `helpers/__init__.py`, export các hàm quan trọng:
   ```python
   from .string_utils import capitalize_words
   from .number_utils import is_prime, factorial
   ```

2. Trong `main.py`, sử dụng:
   ```python
   from helpers import capitalize_words, is_prime
   ```

3. **Yêu cầu**: Code trong `main.py` không được biết bên trong `helpers/` có file `string_utils.py` hay `number_utils.py`

## Bài tập 4: Tránh lỗi thường gặp

### Yêu cầu:
1. Tạo 2 file `module_a.py` và `module_b.py` có circular import
2. Chạy và quan sát lỗi
3. Sửa lại bằng cách tách phần chung ra `module_common.py`

4. Kiểm tra xem có file nào đặt tên trùng với thư viện chuẩn không (ví dụ: `json.py`, `email.py`)
   - Nếu có, đổi tên file

## Bài tập 5: Dự án nhỏ - Quản lý Sách

### Yêu cầu:
Tạo một dự án nhỏ quản lý sách với cấu trúc:

```
library/
├── main.py
├── models/
│   ├── __init__.py
│   └── book.py          # Class Book
└── utils/
    ├── __init__.py
    └── validators.py    # Hàm validate ISBN, validate year
```

1. File `book.py` chứa class `Book` với:
   - Thuộc tính: `title`, `author`, `isbn`, `year`
   - Phương thức: `__str__()`, `is_old()` (sách cũ nếu năm < 2000)

2. File `validators.py` chứa:
   - `validate_isbn(isbn)`: Kiểm tra ISBN hợp lệ (đơn giản: độ dài = 13)
   - `validate_year(year)`: Kiểm tra năm hợp lệ (1900 - 2024)

3. File `models/__init__.py` export class `Book`

4. File `utils/__init__.py` export các hàm validate

5. File `main.py`:
   - Import `Book` từ `models`
   - Import các hàm validate từ `utils`
   - Tạo vài cuốn sách, in thông tin

## Hướng dẫn nộp bài

1. Tạo thư mục `bai_tap_cua_em/` (thay `cua_em` bằng tên của bạn)
2. Đặt tất cả các file bài tập vào thư mục đó
3. Đảm bảo code chạy được không lỗi
4. Comment code rõ ràng

## Tiêu chí chấm điểm

- ✅ Code chạy được, không lỗi
- ✅ Sử dụng đúng các kỹ thuật import
- ✅ Sử dụng `if __name__ == "__main__":` đúng cách
- ✅ Tổ chức code thành package hợp lý
- ✅ Tránh được các lỗi thường gặp
- ✅ Code có comment rõ ràng

