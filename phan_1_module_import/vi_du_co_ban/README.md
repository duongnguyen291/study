# Ví dụ cơ bản về Module và Import

## Mục đích
Ví dụ này minh họa cách Python thực thi code khi import một module.

## Cách chạy

1. Mở terminal trong thư mục này
2. Chạy lệnh:
   ```bash
   python main.py
   ```

## Quan sát kết quả

Bạn sẽ thấy dòng `"Dòng này đang được in ra từ lib.py"` được in ra **trước** cả dòng `"Bắt đầu chương trình chính"`, mặc dù bạn chưa gọi hàm nào trong `lib.py`.

## Bài học

- Khi Python import một module, nó sẽ **thực thi toàn bộ code** trong file đó ngay lập tức.
- Code thực thi (như `print()`, gọi hàm) ở cấp module sẽ chạy khi import.
- Chỉ nên định nghĩa hàm (`def`) và lớp (`class`) trong module, không nên có code thực thi trôi nổi.

## Thử nghiệm

1. Thử comment dòng `print` trong `lib.py` và chạy lại `main.py`
2. Thử thêm một dòng `print` khác ở cuối file `lib.py` và quan sát kết quả

