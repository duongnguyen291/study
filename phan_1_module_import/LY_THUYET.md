# PHẦN 1: TỔ CHỨC MÃ NGUỒN & CƠ CHẾ IMPORT

## 1. Bản chất của Module trong Python

### Định nghĩa
**Module** là một thành phần độc lập, có chức năng riêng biệt, đóng vai trò như một "mảnh ghép" để tạo nên một hệ thống lớn hơn. Việc chia nhỏ một hệ thống thành các module giúp việc quản lý, phát triển và bảo trì dễ dàng hơn, và mỗi module có thể được thêm, bớt, sửa đổi mà ít ảnh hưởng đến các phần khác.

> **Khẳng định quan trọng**: Mọi file có đuôi `.py` đều là một Module.

### 1.1. Tại sao phải chia file? (Tư duy kiến trúc)

Hãy lấy ví dụ: Bạn xây một ngôi nhà.

- **Nếu không chia file**: Bạn vứt tất cả gạch, xi măng, giường, tủ, bát đĩa vào... phòng khách. → Không thể tìm đồ, không thể mở rộng.
- **Nếu chia file**: Phòng ngủ (chứa giường), Nhà kho (chứa gạch), Bếp (chứa bát đĩa). → Dễ bảo trì, dễ thay thế.

**Trong Backend:**
- File xử lý Database (cơ sở dữ liệu) riêng (`database.py`).
- File xử lý Logic nghiệp vụ riêng (`services.py`).
- File định nghĩa API riêng (`routes.py`).

### 1.2. Cơ chế hoạt động của import (Cực kỳ quan trọng)

Khi bạn gõ `import my_module`, Python thực sự làm gì?

1. **Tìm kiếm file**: Python quét trong các thư mục được quy định (biến môi trường `PYTHONPATH` và thư mục hiện tại).
2. **Biên dịch (Compile)**: Chuyển file `.py` thành bytecode `.pyc` (nằm trong thư mục `__pycache__` - thư mục này sinh ra để lần sau chạy nhanh hơn, không phải virus).
3. **Thực thi (Execute)**: Đây là điểm mấu chốt. Python sẽ **chạy từ đầu đến cuối** file được import ngay lập tức.

> ⚠️ **Lưu ý quan trọng**: Python là ngôn ngữ thông dịch, nên code trong module sẽ được thực thi ngay khi import.

**Ví dụ minh họa sự nguy hiểm nếu không hiểu cơ chế thực thi:**

Xem ví dụ trong thư mục `vi_du_co_ban/` để hiểu rõ hơn.

> **Bài học**: Không được viết code thực thi (như `print`, gọi hàm, kết nối DB) trôi nổi trong file module. Chỉ nên định nghĩa hàm (`def`) và lớp (`class`).

## 2. Kỹ thuật Import nâng cao cho Backend

### 2.1. Các kiểu Import và Lời khuyên

Giả sử có file `calculator.py` chứa hàm `add(a, b)` và `sub(a, b)`.

#### Cách 1: Import cả module
```python
import calculator
calculator.add(1, 2)
```
**Ưu điểm**: Rõ ràng nguồn gốc. Biết hàm `add` này là của `calculator` chứ không phải của thư viện khác.  
**Khuyên dùng**: Khi module có nhiều hàm cần dùng.

#### Cách 2: Import cụ thể (Explicit Import)
```python
from calculator import add
add(1, 2)
```
**Ưu điểm**: Code ngắn gọn.  
**Khuyên dùng**: Khi chỉ cần 1-2 hàm. Đây là chuẩn mực của các framework như Django/FastAPI.

#### Cách 3: Import tất cả (Tối kỵ - Anti Pattern)
```python
from calculator import *
```
**Tại sao không nên**: Nếu `calculator` có hàm `open()` và Python cũng có hàm `open()`, hàm của Python sẽ bị đè (overwrite) mà không có báo lỗi.

### 2.2. Alias (Đặt bí danh) - Giải quyết trùng tên

Trong Backend, ta thường xuyên gặp các thư viện trùng tên (ví dụ User model của mình và User của thư viện xác thực).

```python
from my_app.models import User as MyUser
from third_party_auth import User as AuthUser

# Bây giờ có thể dùng cả 2 mà không xung đột
u1 = MyUser()
u2 = AuthUser()
```

## 3. Câu thần chú: `if __name__ == "__main__":`

Đây là khái niệm trừu tượng nhất nhưng bắt buộc phải hiểu.

### Giải thích chi tiết:
- Mỗi file Python có một biến ngầm định tên là `__name__`.
- Nếu file được chạy trực tiếp (Click nút Run hoặc gõ `python file.py`): `__name__` sẽ có giá trị là `"__main__"`.
- Nếu file bị file khác import: `__name__` sẽ có giá trị là tên của file đó (ví dụ `"lib"`).

### Mục đích
Giúp một file vừa có thể chạy độc lập (để test), vừa có thể làm thư viện cho file khác dùng mà không bị chạy code thừa.

**Ví dụ thực tế**: Xem file `database.py` trong thư mục `vi_du_name_main/`.

## 4. Package và Tổ chức thư mục chuẩn Backend

Khi dự án lớn lên, ta không thể để hàng chục file `.py` nằm cùng cấp. Ta cần gom chúng vào các thư mục → Đó là **Package**.

### 4.1. Vai trò của `__init__.py`

- Một thư mục muốn được Python coi là Package (để có thể import từ đó) thì **nên có** file `__init__.py`.
- **Chức năng nâng cao của `__init__.py`** (Dành cho Backend): Nó giống như "Lễ tân" của tòa nhà. Nó quyết định ai ở bên ngoài được gặp ai ở bên trong.

**Ví dụ cấu trúc:**
```
my_backend/
├── main.py
└── features/
    ├── __init__.py
    ├── auth.py (Chứa hàm login)
    └── user.py (Chứa hàm get_profile)
```

Trong `features/__init__.py`, ta có thể viết:
```python
# Gom các hàm quan trọng từ các file con ra "cửa chính"
from .auth import login
from .user import get_profile
```

Lúc này ở `main.py` chỉ cần gọi ngắn gọn:
```python
# Thay vì: from features.auth import login
# Ta dùng:
from features import login
```

→ Giúp che giấu cấu trúc phức tạp bên trong package.

## 5. Lỗi thường gặp (Cần cảnh báo học sinh)

### 5.1. Circular Import (Import vòng tròn)

- **A import B**.
- **B import A**.
- → Python sẽ báo lỗi `ImportError` hoặc kẹt cứng.

**Giải pháp**: Thiết kế lại kiến trúc, tách phần chung ra file C. A và B cùng import C.

Xem ví dụ trong thư mục `loi_thuong_gap/circular_import/`.

### 5.2. Đặt tên file trùng thư viện chuẩn

- Học sinh đặt tên file là `email.py`.
- Trong file đó gõ `import email` (thư viện gửi mail của Python).
- → Python sẽ import chính file hiện tại của học sinh thay vì thư viện chuẩn → Lỗi.

**Giải pháp**: Tránh đặt tên trùng (dùng `my_email.py`, `email_utils.py`).

Xem ví dụ trong thư mục `loi_thuong_gap/trung_ten_thu_vien/`.

## Tổng kết

1. Mọi file `.py` đều là module.
2. Khi import, Python sẽ thực thi toàn bộ code trong file đó.
3. Sử dụng `if __name__ == "__main__":` để tránh code thừa khi import.
4. Package giúp tổ chức code tốt hơn, `__init__.py` là "cửa chính" của package.
5. Tránh circular import và đặt tên file trùng với thư viện chuẩn.

