#!/usr/bin/env python3
"""
Resize & nén ảnh sang WebP trước khi đẩy vào repo ảnh riêng (blog-anh).

Cài đặt (chạy 1 lần):
    pip install pillow

Cách dùng:
    python nen-anh.py <thư_mục_ảnh_gốc> <thư_mục_đích> [--width 1600] [--quality 80]

Ví dụ:
    python nen-anh.py D:\Anh\raw D:\Project\blog-anh\bai-viet\bo-cong-cu

Ảnh sẽ được resize về chiều rộng tối đa (giữ tỉ lệ, không phóng to ảnh nhỏ hơn),
convert sang .webp, và giữ nguyên tên file gốc (đổi đuôi thành .webp).
"""

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("Chưa cài Pillow. Chạy: pip install pillow")

DINH_DANG_HO_TRO = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"}


def nen_anh(duong_dan_vao: Path, duong_dan_ra: Path, max_width: int, quality: int) -> None:
    duong_dan_ra.mkdir(parents=True, exist_ok=True)

    files = [f for f in duong_dan_vao.iterdir() if f.suffix.lower() in DINH_DANG_HO_TRO]
    if not files:
        print(f"Không tìm thấy ảnh nào trong {duong_dan_vao}")
        return

    tong_truoc = 0
    tong_sau = 0

    for f in sorted(files):
        with Image.open(f) as img:
            img = img.convert("RGB") if img.mode in ("P", "RGBA") else img
            w, h = img.size
            if w > max_width:
                new_h = int(h * (max_width / w))
                img = img.resize((max_width, new_h), Image.LANCZOS)

            out_path = duong_dan_ra / (f.stem + ".webp")
            img.save(out_path, "WEBP", quality=quality, method=6)

        truoc = f.stat().st_size
        sau = out_path.stat().st_size
        tong_truoc += truoc
        tong_sau += sau
        print(f"{f.name:35s} {truoc/1024:>8.0f} KB  ->  {out_path.name:35s} {sau/1024:>8.0f} KB")

    print("-" * 90)
    print(f"Tổng: {tong_truoc/1024/1024:.1f} MB -> {tong_sau/1024/1024:.1f} MB "
          f"(giảm {100 * (1 - tong_sau / tong_truoc):.0f}%)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize & nén ảnh sang WebP cho blog.")
    parser.add_argument("nguon", type=Path, help="Thư mục chứa ảnh gốc")
    parser.add_argument("dich", type=Path, help="Thư mục đích (trong repo blog-anh)")
    parser.add_argument("--width", type=int, default=1600, help="Chiều rộng tối đa (px), mặc định 1600")
    parser.add_argument("--quality", type=int, default=80, help="Chất lượng WebP 1-100, mặc định 80")
    args = parser.parse_args()

    if not args.nguon.is_dir():
        sys.exit(f"Không tìm thấy thư mục: {args.nguon}")

    nen_anh(args.nguon, args.dich, args.width, args.quality)
