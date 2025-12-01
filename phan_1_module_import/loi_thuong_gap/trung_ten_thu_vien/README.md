# Lỗi đặt tên file trùng với thư viện chuẩn

## Mục đích
Ví dụ này minh họa lỗi khi đặt tên file trùng với thư viện chuẩn của Python.

## Vấn đề

### Tại sao lại lỗi?
- Bạn đặt tên file là `email.py`
- Trong file đó, bạn muốn import thư viện `email` của Python
- **Python sẽ import chính file `email.py` của bạn** thay vì thư viện chuẩn!
- → Lỗi `AttributeError` vì file của bạn không có các hàm của thư viện chuẩn

### Ví dụ lỗi

**email.py** (tên file trùng với thư viện):
```python
import email  # ❌ Python import chính file này!
```

Khi chạy sẽ báo lỗi vì file `email.py` không có các class như `email.message.EmailMessage`.

## Cách chạy (để xem lỗi)

```bash
# Sẽ báo lỗi AttributeError
python email.py
```

**Lỗi sẽ là:**
```
❌ Lỗi: module 'email' has no attribute 'message'
Python đã import chính file email.py này thay vì thư viện chuẩn!
```

## Giải pháp

### Đổi tên file
Thay vì `email.py`, dùng:
- `my_email.py`
- `email_utils.py`
- `email_helper.py`
- `send_email.py`
- `email_service.py`

Xem file `email_utils.py` để thấy cách đúng.

## Các tên file cần tránh

Các tên này trùng với thư viện chuẩn của Python, **KHÔNG NÊN** đặt tên file như vậy:

- `email.py` → Dùng `email_utils.py`
- `json.py` → Dùng `json_utils.py`
- `sys.py` → Dùng `system_utils.py`
- `os.py` → Dùng `os_utils.py`
- `math.py` → Dùng `math_utils.py`
- `random.py` → Dùng `random_utils.py`
- `datetime.py` → Dùng `datetime_utils.py`
- `time.py` → Dùng `time_utils.py`
- `string.py` → Dùng `string_utils.py`
- `collections.py` → Dùng `collections_utils.py`

## Bài học

1. **Kiểm tra tên file**: Trước khi đặt tên, kiểm tra xem có trùng với thư viện chuẩn không
2. **Đặt tên rõ ràng**: Dùng tên mô tả rõ chức năng (ví dụ: `email_utils.py` thay vì `email.py`)
3. **Khi gặp lỗi lạ**: Nếu import thư viện chuẩn bị lỗi, kiểm tra xem có file nào trùng tên không

## Thực hành

1. Thử chạy `email.py` để xem lỗi
2. Chạy `email_utils.py` để xem cách đúng
3. Thử đổi tên file `email.py` thành `my_email.py` và xem kết quả

