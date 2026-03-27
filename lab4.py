from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

from common.config import DEFAULT_REPORT_IMAGE_COUNT, INPUT_DIR, LAB4_THRESHOLD, LAB4_VARIANT, ROOT_DIR
from common.input_source import ensure_input_images
from common.image_ops import normalize_to_uint8, roberts_cross_gradients, weighted_grayscale
from common.io_utils import copy_source_image, load_rgb_image, save_gray_image
from common.report_utils import markdown_image, write_markdown


def run(input_dir: Path, limit: int | None = None, report_images: int = DEFAULT_REPORT_IMAGE_COUNT) -> None:
    image_paths = ensure_input_images(input_dir, limit=limit)
    if not image_paths:
        raise SystemExit(f"No input images found in {input_dir}")

    lab_dir = ROOT_DIR / "lab4"
    images_dir = lab_dir / "images"
    grayscale_dir = images_dir / "grayscale"
    gx_dir = images_dir / "Gx"
    gy_dir = images_dir / "Gy"
    g_dir = images_dir / "G"
    g_binary_dir = images_dir / "G_binary"

    report_items: list[dict[str, Path | int]] = []
    for index, source_path in enumerate(image_paths):
        image = load_rgb_image(source_path)
        source_out = images_dir / f"{index}.png"
        gray_out = grayscale_dir / f"{index}.png"
        gx_out = gx_dir / f"{index}.png"
        gy_out = gy_dir / f"{index}.png"
        g_out = g_dir / f"{index}.png"
        g_binary_out = g_binary_dir / f"{index}.png"

        copy_source_image(source_path, source_out)
        grayscale = weighted_grayscale(image)
        gx_raw, gy_raw = roberts_cross_gradients(grayscale)
        gradient_raw = np.abs(gx_raw) + np.abs(gy_raw)

        gx = normalize_to_uint8(np.abs(gx_raw))
        gy = normalize_to_uint8(np.abs(gy_raw))
        gradient = normalize_to_uint8(gradient_raw)
        binary_gradient = np.where(gradient >= LAB4_THRESHOLD, 255, 0).astype(np.uint8)

        save_gray_image(gray_out, grayscale)
        save_gray_image(gx_out, gx)
        save_gray_image(gy_out, gy)
        save_gray_image(g_out, gradient)
        save_gray_image(g_binary_out, binary_gradient)

        report_items.append(
            {
                "index": index,
                "source": source_out,
                "gray": gray_out,
                "gx": gx_out,
                "gy": gy_out,
                "g": g_out,
                "binary": g_binary_out,
            }
        )

    lines = [
        "# Лабораторная работа №4",
        f"## Вариант {LAB4_VARIANT}. Выделение контуров на изображении",
        "",
        "Использован оператор Робертса `2x2` с формулой варианта 2:",
        "- `Gx = I(x, y) - I(x + 1, y + 1)`",
        "- `Gy = I(x, y + 1) - I(x + 1, y)`",
        "- `G = |Gx| + |Gy|`",
        "",
        f"Порог бинаризации итогового градиента: `T = {LAB4_THRESHOLD}`.",
        "",
    ]

    for item in report_items[:report_images]:
        index = item["index"]
        lines.extend(
            [
                f"### Изображение {index}",
                "",
                "| Исходное | Полутоновое | Бинарное G |",
                "|:--------:|:-----------:|:----------:|",
                (
                    f"| {markdown_image(item['source'], f'src{index}')} | "
                    f"{markdown_image(item['gray'], f'gray{index}')} | "
                    f"{markdown_image(item['binary'], f'gbin{index}')} |"
                ),
                "",
                "| Gx | Gy | G |",
                "|:--:|:--:|:--:|",
                (
                    f"| {markdown_image(item['gx'], f'gx{index}')} | "
                    f"{markdown_image(item['gy'], f'gy{index}')} | "
                    f"{markdown_image(item['g'], f'g{index}')} |"
                ),
                "",
            ]
        )

    lines.extend(
        [
            "### Вывод",
            "",
            "Для варианта 2 построены градиентные карты Робертса `Gx`, `Gy`, итоговый градиент `G` и бинаризованные контуры.",
        ]
    )
    write_markdown(ROOT_DIR / "lab4.md", lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run lab 4.")
    parser.add_argument("--input-dir", type=Path, default=INPUT_DIR, help="Directory with source images.")
    parser.add_argument("--limit", type=int, default=None, help="Process only the first N images.")
    parser.add_argument(
        "--report-images",
        type=int,
        default=DEFAULT_REPORT_IMAGE_COUNT,
        help="How many processed images to include into the markdown report.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    run(args.input_dir, limit=args.limit, report_images=args.report_images)
    print("lab4 complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
