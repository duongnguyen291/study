# Ví dụ về `if __name__ == "__main__":`

## Mục đích
Ví dụ này minh họa cách một file Python vừa có thể chạy độc lập (để test), vừa có thể làm thư viện cho file khác.

## Cách chạy

### 1. Chạy trực tiếp database.py
```bash
python database.py
```

**Kết quả**: Bạn sẽ thấy:
- `__name__ = "__main__"`
- Code trong `if __name__ == "__main__":` được thực thi
- In ra "=== ĐANG TEST KẾT NỐI DB ==="

### 2. Chạy main.py (import database)
```bash
python main.py
```

**Kết quả**: Bạn sẽ thấy:
- `__name__ = "database"` (không phải `"__main__"`)
- Code trong `if __name__ == "__main__":` của database.py **KHÔNG chạy**
- Chỉ có code định nghĩa hàm và code ngoài if mới chạy

## Giải thích

- **`__name__`** là biến đặc biệt của Python
- Khi file được chạy trực tiếp: `__name__ = "__main__"`
- Khi file được import: `__name__ = tên_file` (ví dụ: `"database"`)

## Ứng dụng thực tế

- **Test code**: Viết code test trong `if __name__ == "__main__":` để test module
- **Tránh code thừa**: Code quan trọng (như kết nối DB) chỉ chạy khi cần thiết
- **Module linh hoạt**: Một file vừa là script, vừa là thư viện

## Bài học

Luôn sử dụng `if __name__ == "__main__":` cho code test hoặc code chỉ chạy khi file được thực thi trực tiếp.

