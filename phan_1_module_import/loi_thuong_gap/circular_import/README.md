# Lỗi Circular Import (Import vòng tròn)

## Mục đích
Ví dụ này minh họa lỗi Circular Import và cách khắc phục.

## Vấn đề

### Circular Import là gì?
- **File A** import **File B**
- **File B** import **File A**
- → Tạo ra vòng tròn, Python không biết load file nào trước → **Lỗi!**

### Ví dụ lỗi

**file_a.py:**
```python
from file_b import function_b  # Import B
```

**file_b.py:**
```python
from file_a import function_a  # Import A -> VÒNG TRÒN!
```

## Cách chạy (để xem lỗi)

```bash
# Sẽ báo lỗi ImportError
python file_a.py
# hoặc
python file_b.py
```

**Lỗi sẽ là:**
```
ImportError: cannot import name 'function_a' from partially initialized module 'file_a'
```

## Giải pháp

### Cách 1: Tách phần chung ra file riêng

Tạo file `file_common.py` chứa phần chung, cả A và B cùng import file này.

**file_common.py:**
```python
def common_function():
    print("Đây là hàm chung")
```

**file_a_fixed.py:**
```python
from file_common import common_function  # Import file chung
```

**file_b_fixed.py:**
```python
from file_common import common_function  # Import file chung
```

### Cách 2: Di chuyển import vào trong hàm

Thay vì import ở đầu file, import bên trong hàm khi cần:

```python
def function_a():
    from file_b import function_b  # Import khi cần
    function_b()
```

### Cách 3: Thiết kế lại kiến trúc

- Xem xét lại mối quan hệ giữa các module
- Tách phần chung ra module riêng
- Sử dụng dependency injection nếu cần

## Bài học

1. **Tránh Circular Import**: Không để A import B và B import A
2. **Tách phần chung**: Nếu A và B cần dùng chung, tách ra file C
3. **Thiết kế tốt**: Circular Import thường là dấu hiệu của thiết kế chưa tốt

## Thực hành

1. Thử chạy `file_a.py` để xem lỗi
2. Chạy `file_a_fixed.py` để xem cách sửa
3. So sánh sự khác biệt

