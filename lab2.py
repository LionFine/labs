from __future__ import annotations

import argparse
from pathlib import Path

from common.config import DEFAULT_REPORT_IMAGE_COUNT, INPUT_DIR, LAB2_VARIANT, ROOT_DIR
from common.input_source import ensure_input_images
from common.image_ops import global_threshold_binarize, otsu_threshold, weighted_grayscale
from common.io_utils import copy_source_image, load_rgb_image, save_gray_image
from common.report_utils import markdown_image, write_markdown


def run(input_dir: Path, limit: int | None = None, report_images: int = DEFAULT_REPORT_IMAGE_COUNT) -> None:
    image_paths = ensure_input_images(input_dir, limit=limit)
    if not image_paths:
        raise SystemExit(f"No input images found in {input_dir}")

    lab_dir = ROOT_DIR / "lab2"
    images_dir = lab_dir / "images"
    grayscale_dir = images_dir / "grayscale"
    binary_dir = images_dir / "binary"

    report_items: list[dict[str, Path | int]] = []
    thresholds: list[int] = []
    for index, source_path in enumerate(image_paths):
        image = load_rgb_image(source_path)
        source_out = images_dir / f"{index}.png"
        gray_out = grayscale_dir / f"{index}.png"
        binary_out = binary_dir / f"{index}.png"

        copy_source_image(source_path, source_out)
        grayscale = weighted_grayscale(image)
        threshold = otsu_threshold(grayscale)
        binary = global_threshold_binarize(grayscale, threshold)

        save_gray_image(gray_out, grayscale)
        save_gray_image(binary_out, binary)

        thresholds.append(threshold)
        report_items.append(
            {
                "index": index,
                "source": source_out,
                "gray": gray_out,
                "binary": binary_out,
                "threshold": threshold,
            }
        )

    lines = [
        "# Лабораторная работа №2",
        f"## Вариант {LAB2_VARIANT}. Обесцвечивание и бинаризация растровых изображений",
        "",
        "Для изображений выполнены:",
        "- перевод полноцветного изображения в полутоновое по взвешенному среднему каналов;",
        "- глобальная бинаризация по критерию Отсу.",
        "",
        "Порог бинаризации определяется автоматически по гистограмме яркости для каждого изображения.",
        "",
    ]

    for item in report_items[:report_images]:
        index = item["index"]
        threshold = item["threshold"]
        lines.extend(
            [
                f"### Изображение {index}",
                "",
                f"Порог Отсу: `T = {threshold}`.",
                "",
                "| Исходное | Полутоновое | Бинарное |",
                "|:--------:|:-----------:|:--------:|",
                (
                    f"| {markdown_image(item['source'], f'src{index}')} | "
                    f"{markdown_image(item['gray'], f'gray{index}')} | "
                    f"{markdown_image(item['binary'], f'bin{index}')} |"
                ),
                "",
            ]
        )

    lines.extend(
        [
            "### Вывод",
            "",
            "Получены полутоновые изображения и результат глобальной пороговой обработки по критерию Отсу для варианта 2.",
        ]
    )
    write_markdown(ROOT_DIR / "lab2.md", lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run lab 2.")
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
    print("lab2 complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
