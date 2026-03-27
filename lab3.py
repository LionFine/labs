from __future__ import annotations

import argparse
from pathlib import Path

from common.config import DEFAULT_REPORT_IMAGE_COUNT, INPUT_DIR, LAB3_VARIANT, LAB3_WINDOW_SIZE, ROOT_DIR
from common.input_source import ensure_input_images
from common.image_ops import absolute_difference, conservative_smoothing, normalize_to_uint8, weighted_grayscale
from common.io_utils import copy_source_image, load_rgb_image, save_gray_image
from common.report_utils import markdown_image, write_markdown


def run(input_dir: Path, limit: int | None = None, report_images: int = DEFAULT_REPORT_IMAGE_COUNT) -> None:
    image_paths = ensure_input_images(input_dir, limit=limit)
    if not image_paths:
        raise SystemExit(f"No input images found in {input_dir}")

    lab_dir = ROOT_DIR / "lab3"
    images_dir = lab_dir / "images"
    grayscale_dir = images_dir / "grayscale"
    filtered_dir = images_dir / "filtered_grayscale"
    diff_dir = images_dir / "diff_grayscale_abs"

    report_items: list[dict[str, Path | int]] = []
    for index, source_path in enumerate(image_paths):
        image = load_rgb_image(source_path)
        source_out = images_dir / f"{index}.png"
        gray_out = grayscale_dir / f"{index}.png"
        filtered_out = filtered_dir / f"{index}.png"
        diff_out = diff_dir / f"{index}.png"

        copy_source_image(source_path, source_out)
        grayscale = weighted_grayscale(image)
        filtered = conservative_smoothing(grayscale, LAB3_WINDOW_SIZE)
        diff = normalize_to_uint8(absolute_difference(grayscale, filtered))

        save_gray_image(gray_out, grayscale)
        save_gray_image(filtered_out, filtered)
        save_gray_image(diff_out, diff)

        report_items.append(
            {
                "index": index,
                "source": source_out,
                "gray": gray_out,
                "filtered": filtered_out,
                "diff": diff_out,
            }
        )

    lines = [
        "# Лабораторная работа №3",
        f"## Вариант {LAB3_VARIANT}. Фильтрация изображений и морфологические операции",
        "",
        f"Реализовано консервативное сглаживание с окном `{LAB3_WINDOW_SIZE}x{LAB3_WINDOW_SIZE}`.",
        "",
        "Подготовка входных данных:",
        "- исходное цветное изображение приведено к полутоновому виду;",
        "- фильтр применяется к полутоновому изображению;",
        "- разностное изображение построено как модуль разности и дополнительно нормализовано для лучшей видимости изменений.",
        "",
    ]

    for item in report_items[:report_images]:
        index = item["index"]
        lines.extend(
            [
                f"### Изображение {index}",
                "",
                "| Исходное | Полутоновое | После фильтрации |",
                "|:--------:|:-----------:|:----------------:|",
                (
                    f"| {markdown_image(item['source'], f'src{index}')} | "
                    f"{markdown_image(item['gray'], f'gray{index}')} | "
                    f"{markdown_image(item['filtered'], f'filtered{index}')} |"
                ),
                "",
                "| Модуль разности |",
                "|:---------------:|",
                f"| {markdown_image(item['diff'], f'diff{index}')} |",
                "",
            ]
        )

    lines.extend(
        [
            "### Вывод",
            "",
            "Для варианта 2 выполнено консервативное сглаживание полутоновых изображений. Получены отфильтрованные изображения и карты изменений после обработки.",
        ]
    )
    write_markdown(ROOT_DIR / "lab3.md", lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run lab 3.")
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
    print("lab3 complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
