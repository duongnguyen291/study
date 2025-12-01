# PHẦN 2: LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG (OOP)

## Chủ đề: Thế giới Lập trình là một xưởng sản xuất

### 1. Mở đầu: Class (Cái khuôn) và Object (Sản phẩm)

Hãy tưởng tượng em đang chơi trò nặn đất sét hoặc làm bánh quy.

- **Class (Lớp)**: Chính là cái **Khuôn cắt bánh**.
  - Cái khuôn này chỉ là kim loại/nhựa, em không thể ăn cái khuôn được.
  - Nó quy định hình dáng: Ngôi sao, Trái tim, hay Hình tròn.

- **Object (Đối tượng)**: Chính là **Những chiếc bánh quy** được tạo ra từ cái khuôn đó.
  - Em có thể tạo ra 100 cái bánh từ 1 cái khuôn.
  - Cái bánh thì ăn được (có thật), còn cái khuôn chỉ là mẫu thôi.

**Trong Python:**
- `class Robot:` (Đây là bản vẽ thiết kế Robot).
- `robot_a = Robot()` (Đây là con Robot A thật sự được lắp ráp xong).

### 2. Đặc điểm (Thuộc tính) và Hành động (Phương thức)

Hãy tưởng tượng em đang tạo nhân vật trong Game (như Minecraft, Roblox hay Liên Quân).

Một nhân vật (Object) sẽ luôn có 2 phần:

1. **Nó trông như thế nào?** (Mắt xanh, tóc đỏ, máu 100, năng lượng 50...) 
   - Trong lập trình gọi là **Thuộc tính (Attribute)**.

2. **Nó làm được gì?** (Chạy, Nhảy, Bắn súng, Hồi máu...) 
   - Trong lập trình gọi là **Phương thức (Method)**.

Xem ví dụ trong thư mục `vi_du_co_ban/nhan_vat_game.py`.

### 3. Kế thừa (Inheritance): "Con nhà tông, không giống lông cũng giống cánh"

Hãy tưởng tượng về gia đình.

- **Bố (Class Cha)**: Biết "Ăn", biết "Ngủ".
- **Con (Class Con)**: Sinh ra là đã biết "Ăn" và "Ngủ" giống bố rồi (không cần học lại). Nhưng người con còn biết thêm "Chơi Game", "Lướt TikTok" (cái mà bố không biết).

**Trong Lập trình**: Giúp em lười biếng một cách thông minh! Em viết code cho con Vật (Animal) biết chạy. Sau đó em tạo con Chó, con Mèo kế thừa từ con Vật. Thế là Chó, Mèo tự nhiên biết chạy mà không cần code lại dòng nào.

Xem ví dụ trong thư mục `vi_du_ke_thua/`.

### 4. Đóng gói (Encapsulation): Cái vỏ bảo vệ

Hãy nhìn chiếc điện thoại smartphone của em.

- **Bên ngoài (Public)**: Màn hình cảm ứng, nút bấm. Em tha hồ chạm vào để chơi game.
- **Bên trong (Private)**: Mạch điện, pin, dây nối loằng ngoằng.
  - Nhà sản xuất đã "Đóng gói" kỹ các mạch điện bên trong lớp vỏ.
  - Tại sao? Vì nếu để hở ra, em tò mò lấy kéo cắt dây hoặc đổ nước vào thì điện thoại hỏng ngay!

**Trong Lập trình**: Có những dữ liệu quan trọng (như mật khẩu, số tiền trong ví) phải được giấu đi (Private), không cho phép sửa lung tung từ bên ngoài. Muốn sửa phải đi qua "cửa chính" (các hàm cho phép).

Xem ví dụ trong thư mục `vi_du_dong_goi/`.

## Dự án thực hành: Xây dựng Backend cho Quán Trà Sữa

### 1. Tư duy thiết kế (Modeling)

Trước khi code, hãy hỏi: "Để quản lý quán trà sữa, chúng ta cần những đối tượng nào?"

- **Món đồ uống**: Tên là gì? Giá bao nhiêu? Size gì? → Class `TraSua`
- **Hóa đơn**: Chứa danh sách các món đã gọi, tính tổng tiền. → Class `HoaDon`
- **Khách hàng**: Tên, hạng thành viên (để giảm giá). → Class `KhachHang`

### 2. Bước 1: Tạo đối tượng dữ liệu (Data Object)

Đầu tiên, tạo class đại diện cho ly trà sữa. Đây là thành phần nhỏ nhất.

Xem file `du_an_tra_sua/models/tra_sua.py`.

**Giải thích**: `__str__` là một "magic method" (phương thức đặc biệt). Khi em `print(ly_tra_sua)`, Python sẽ tự động gọi hàm này để hiển thị nội dung.

### 3. Bước 2: Tạo đối tượng quản lý (Manager Object) - Quan trọng!

Đây là phần các bạn mới học hay vấp. Làm sao để quản lý nhiều ly trà sữa? Ta cần một class `HoaDon` chứa một List các ly trà sữa.

Xem file `du_an_tra_sua/models/hoa_don.py`.

**Điểm chốt**: 
- `self.danh_sach_mon` là một LIST rỗng để chứa các object `TraSua`.
- Khi cần lấy giá, ta lôi từng ly trà sữa ra và hỏi `mon.gia`.

### 4. Bước 3: Kế thừa để xử lý Khách VIP

Giả sử quán có chương trình: Khách VIP được giảm 10%. Ta sẽ tạo class `HoaDonVIP` kế thừa logic thanh toán.

**Tư duy**: Thay vì viết lại hàm tính tiền, ta chỉ cần "ghi đè" (override) logic tính tiền cuối cùng.

Xem file `du_an_tra_sua/models/hoa_don_vip.py`.

### 5. Giải thích kỹ thuật cho Học sinh (Điểm chốt)

1. **Object trong Object**:
   - `self.danh_sach_mon.append(mon)` - List này không chứa số hay chữ, mà nó chứa hẳn những ly trà sữa (object).
   - Khi cần lấy giá, ta lôi từng ly trà sữa ra và hỏi `mon.gia`.

2. **Tại sao phải chia Class? Sao không viết hết 1 cục?**
   - Nếu sếp bảo: "Món trà sữa bây giờ có thêm topping". Em chỉ cần vào class `TraSua` sửa đúng 1 chỗ.
   - Nếu sếp bảo: "Đổi công thức giảm giá VIP". Em chỉ cần vào class `HoaDonVIP` sửa đúng 1 dòng.
   - → Đây là tư duy **Dễ bảo trì (Maintainable)** của Backend Engineer.

## Tổng kết

1. **Class** là khuôn mẫu, **Object** là sản phẩm được tạo ra từ khuôn.
2. **Thuộc tính (Attribute)**: Mô tả đặc điểm của object.
3. **Phương thức (Method)**: Mô tả hành động của object.
4. **Kế thừa (Inheritance)**: Class con kế thừa từ class cha, tránh code lặp lại.
5. **Đóng gói (Encapsulation)**: Bảo vệ dữ liệu quan trọng, chỉ cho phép truy cập qua "cửa chính".

## Bài tập mở rộng

Xem thư mục `bai_tap_mo_rong/` để có hướng dẫn mở rộng hệ thống Quán Trà Sữa.

