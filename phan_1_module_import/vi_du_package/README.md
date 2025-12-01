# Ví dụ về Package và __init__.py

## Mục đích
Ví dụ này minh họa cách tổ chức code thành package và vai trò của `__init__.py`.

## Cấu trúc

```
my_backend/
├── main.py
└── features/
    ├── __init__.py    # "Lễ tân" của package
    ├── auth.py        # Module xử lý xác thực
    └── user.py        # Module xử lý user
```

## Cách chạy

```bash
cd my_backend
python main.py
```

## Giải thích

### Vai trò của __init__.py

1. **Đánh dấu thư mục là Package**: Python biết `features` là một package, không phải thư mục thường.

2. **"Lễ tân" của package**: File `__init__.py` quyết định ai ở bên ngoài được gặp ai ở bên trong.

3. **Che giấu cấu trúc phức tạp**: 
   - Bên ngoài chỉ cần: `from features import login`
   - Không cần biết bên trong có file `auth.py` hay `user.py`

### Import với dấu chấm (.)

Trong `__init__.py`:
```python
from .auth import login  # Dấu chấm (.) = cùng package
```

- `.auth` nghĩa là file `auth.py` trong cùng package `features`
- Tương đương với `from features.auth import login` nhưng ngắn gọn hơn

## Ưu điểm

1. **Dễ bảo trì**: Nếu đổi tên file `auth.py` -> `authentication.py`, chỉ cần sửa `__init__.py`
2. **Che giấu chi tiết**: Code bên ngoài không cần biết cấu trúc bên trong
3. **Tổ chức tốt**: Dễ quản lý khi dự án lớn

## Bài học

- Package giúp tổ chức code tốt hơn khi dự án lớn
- `__init__.py` là "cửa chính" của package, quyết định export gì ra ngoài
- Sử dụng dấu chấm (.) để import từ cùng package

