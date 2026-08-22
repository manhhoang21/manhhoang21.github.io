---
title: "Đà Lạt — ba ngày không lịch trình"
category: duong
location: "Đà Lạt, Lâm Đồng"
days: 3
permalink: /chuyen-di/da-lat-2026-03/
# Ảnh bìa: đường dẫn tính từ gốc repo blog-anh, không cần https đầy đủ.
# Trang /chuyen-di/ sẽ tự ghép với site.cdn_url trong _config.yml.
cover: chuyen-di/da-lat-2026-03/bia.webp
---

Đoạn đầu này được lấy làm tóm tắt hiện trên trang Chuyến đi, nên viết gọn
và có hình ảnh một chút — chừng 2 tới 3 câu là vừa.

## Ngày 1

Chèn ảnh bằng include, `src` là đường dẫn trong repo blog-anh:

{% include img.html src="chuyen-di/da-lat-2026-03/01.webp" alt="Chợ đêm lúc 9 giờ" %}

Muốn có chú thích dưới ảnh thì thêm `caption`:

{% include img.html src="chuyen-di/da-lat-2026-03/02.webp" alt="Đường lên đồi chè" caption="Đường lên đồi chè, sáng sớm còn sương." %}

## Ngày 2

Xếp nhiều ảnh thành lưới thì bọc trong div `gallery`:

<div class="gallery">
{% include img.html src="chuyen-di/da-lat-2026-03/03.webp" alt="" %}
{% include img.html src="chuyen-di/da-lat-2026-03/04.webp" alt="" %}
{% include img.html src="chuyen-di/da-lat-2026-03/05.webp" alt="" %}
</div>

## Ngày 3

Đoạn kết.

---

**Quy trình thêm một chuyến đi**

1. Nén ảnh: `python scripts/nen-anh.py D:\Anh\raw D:\Project\blog-anh\chuyen-di\da-lat-2026-03`
2. Commit và push repo `blog-anh`
3. Copy file này sang `_posts/` đặt tên `2026-03-15-da-lat.md`, sửa nội dung
4. Ảnh tự hiện qua jsDelivr, không cần đợi gì thêm
