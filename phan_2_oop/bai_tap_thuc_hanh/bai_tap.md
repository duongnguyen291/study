# Bài tập thực hành - PHẦN 2: Lập trình hướng đối tượng (OOP)

## Bài tập 1: Class và Object cơ bản

### Yêu cầu:
Tạo class `XeMay` với:
- **Thuộc tính**: `hang_xe`, `mau_sac`, `gia`, `so_km`
- **Phương thức**: 
  - `chay(km)`: Tăng số km lên
  - `xem_thong_tin()`: In thông tin xe
  - `tinh_gia_tri_con_lai()`: Giá trị còn lại = giá - (số_km * 0.1)

Tạo 2 object `XeMay` và test các phương thức.

## Bài tập 2: Kế thừa

### Yêu cầu:
1. Tạo class `DongVat` với:
   - Thuộc tính: `ten`, `tuoi`
   - Phương thức: `an()`, `ngu()`, `keu()`

2. Tạo class `Cho` kế thừa từ `DongVat`:
   - Ghi đè `keu()`: In "Gâu gâu!"
   - Thêm phương thức: `duoi_meo()`

3. Tạo class `Meo` kế thừa từ `DongVat`:
   - Ghi đè `keu()`: In "Meo meo!"
   - Thêm phương thức: `bat_chuot()`

4. Tạo object và test các phương thức.

## Bài tập 3: Đóng gói (Encapsulation)

### Yêu cầu:
Tạo class `TaiKhoan` với:
- **Private thuộc tính**: `__so_tien`, `__mat_khau`
- **Public thuộc tính**: `ten_chu_tai_khoan`
- **Public phương thức**:
  - `nap_tien(so_tien, mat_khau)`: Nạp tiền (cần mật khẩu)
  - `rut_tien(so_tien, mat_khau)`: Rút tiền (cần mật khẩu, kiểm tra số dư)
  - `xem_so_du(mat_khau)`: Xem số dư (cần mật khẩu)
  - `doi_mat_khau(mat_khau_cu, mat_khau_moi)`: Đổi mật khẩu

Test các phương thức và thử truy cập trực tiếp `__so_tien` (sẽ không được).

## Bài tập 4: Dự án Quán Trà Sữa - Mở rộng

### Yêu cầu:
Dựa trên dự án Quán Trà Sữa, thực hiện:

1. **Tạo class HoaDonThanThiet** (giảm 5%):
   - Kế thừa từ `HoaDon`
   - Ghi đè `tinh_tong_tien()` để giảm 5%
   - Ghi đè `in_hoa_don()` để hiển thị "HÓA ĐƠN THÂN THIẾT"

2. **Mở rộng class TraSua**:
   - Thêm thuộc tính `loai_duong` ("Ít đường", "Bình thường", "Nhiều đường")
   - Nếu "Nhiều đường", cộng thêm 2k

3. **Mở rộng class KhachHang**:
   - Thêm phương thức `kiem_tra_than_thiet()`: Nếu tổng tiền đã mua > 500k, tự động nâng cấp lên "Thân thiết"
   - Thêm phương thức `tinh_diem_tich_luy()`: Mỗi 10k = 1 điểm

4. **Tạo class Menu**:
   - Thuộc tính: `danh_sach_mon` (List các TraSua)
   - Phương thức:
     - `them_mon(tra_sua)`: Thêm món vào menu
     - `hien_thi_menu()`: Hiển thị menu
     - `tim_mon(ten)`: Tìm món theo tên

## Bài tập 5: Dự án nhỏ - Quản lý Thư viện

### Yêu cầu:
Tạo hệ thống quản lý thư viện với các class:

1. **Class Sach**:
   - Thuộc tính: `ten`, `tac_gia`, `nam_xuat_ban`, `so_trang`, `tinh_trang` ("Có sẵn", "Đã mượn")
   - Phương thức: `muon_sach()`, `tra_sach()`, `__str__()`

2. **Class DocGia**:
   - Thuộc tính: `ten`, `ma_doc_gia`, `danh_sach_sach_dang_muon` (List)
   - Phương thức: 
     - `muon_sach(sach)`: Mượn sách (kiểm tra tình trạng)
     - `tra_sach(sach)`: Trả sách
     - `xem_sach_dang_muon()`: Xem danh sách sách đang mượn

3. **Class ThuVien**:
   - Thuộc tính: `danh_sach_sach` (List), `danh_sach_doc_gia` (List)
   - Phương thức:
     - `them_sach(sach)`: Thêm sách vào thư viện
     - `them_doc_gia(doc_gia)`: Thêm độc giả
     - `tim_sach(ten)`: Tìm sách theo tên
     - `thong_ke()`: Thống kê số sách, số độc giả

4. **Class SachGiaoKhoa** (kế thừa từ Sach):
   - Thêm thuộc tính: `lop`, `mon_hoc`
   - Ghi đè `__str__()` để hiển thị thêm thông tin lớp và môn học

## Hướng dẫn nộp bài

1. Tạo thư mục `bai_tap_cua_em/` (thay `cua_em` bằng tên của bạn)
2. Tạo file riêng cho mỗi bài tập:
   - `bai_tap_1_xe_may.py`
   - `bai_tap_2_ke_thua.py`
   - `bai_tap_3_encapsulation.py`
   - `bai_tap_4_tra_sua_mo_rong/` (thư mục)
   - `bai_tap_5_thu_vien/` (thư mục)
3. Đảm bảo code chạy được không lỗi
4. Comment code rõ ràng

## Tiêu chí chấm điểm

- ✅ Code chạy được, không lỗi
- ✅ Sử dụng đúng Class, Object, Attribute, Method
- ✅ Sử dụng đúng Kế thừa và Ghi đè
- ✅ Sử dụng đúng Encapsulation (Public/Private)
- ✅ Code có comment rõ ràng
- ✅ Tổ chức code hợp lý (chia file, package nếu cần)

## Gợi ý

1. **Bắt đầu từ đơn giản**: Làm bài tập 1, 2, 3 trước
2. **Tham khảo code mẫu**: Xem các ví dụ trong thư mục `vi_du_*`
3. **Test kỹ**: Tạo file test cho mỗi class
4. **Đọc kỹ yêu cầu**: Đảm bảo làm đúng yêu cầu

## Tài liệu tham khảo

- Xem `LY_THUYET.md` để ôn lại lý thuyết
- Xem các ví dụ trong `vi_du_co_ban/`, `vi_du_ke_thua/`, `vi_du_dong_goi/`
- Xem dự án mẫu trong `du_an_tra_sua/`

