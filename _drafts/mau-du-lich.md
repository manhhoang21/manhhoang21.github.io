---
title: "Đà Lạt — ba ngày không lịch trình"
# Hai dòng dưới chỉ để xem trước bản nháp (--drafts). Khi đăng có thể xoá:
# bài nằm trong _posts/du-lich/ tự có danh mục, layout và URL /trai-nghiem/du-lich/<tên-bài>/.
category: duong
layout: trai-nghiem

# Ảnh bìa: đường dẫn tính từ gốc repo blog-anh, không cần https đầy đủ.
cover: du-lich/da-lat-2026-03/bia.webp

# Hộp thông tin đầu bài. Trường nào không có thì xoá dòng đó, hộp tự ẩn dòng tương ứng.
location: "Đà Lạt, Lâm Đồng"   # hiện cả trên thẻ ở trang danh sách
days: 3                        # hiện cả trên thẻ, tự thêm chữ "ngày"
budget: "khoảng 3,5 triệu / người"
transport: "Xe giường nằm + thuê xe máy"
season: "Tháng 12 – 3, ít mưa"
---

Đoạn đầu này được lấy làm tóm tắt trên trang Du lịch và trang Trải nghiệm, nên viết gọn
và có hình ảnh một chút — chừng 2 tới 3 câu là vừa.

## Ngày 1

Chèn ảnh bằng include, `src` là đường dẫn trong repo blog-anh:

{% include img.html src="du-lich/da-lat-2026-03/01.webp" alt="Chợ đêm lúc 9 giờ" %}

Muốn có chú thích dưới ảnh thì thêm `caption`:

{% include img.html src="du-lich/da-lat-2026-03/02.webp" alt="Đường lên đồi chè" caption="Đường lên đồi chè, sáng sớm còn sương." %}

## Ngày 2

Xếp nhiều ảnh thành lưới thì bọc trong div `gallery`:

<div class="gallery">
{% include img.html src="du-lich/da-lat-2026-03/03.webp" alt="" %}
{% include img.html src="du-lich/da-lat-2026-03/04.webp" alt="" %}
{% include img.html src="du-lich/da-lat-2026-03/05.webp" alt="" %}
</div>

## Ngày 3

Đoạn kết: nếu đi lại thì làm gì khác.

---

**Cách đăng một chuyến đi** (không theo lịch — đăng khi nào muốn chia sẻ)

1. Nén ảnh: `python scripts/nen-anh.py D:\Anh\raw D:\Project\blog-anh\du-lich\da-lat-2026-03`
2. Commit và push repo `blog-anh`
3. Copy file này sang `_posts/du-lich/`, đặt tên `2026-03-15-da-lat.md`, sửa nội dung, xoá phần hướng dẫn này
4. Bài tự hiện ở /trai-nghiem/du-lich/, trang tổng /trai-nghiem/ và trang chủ
