#!/usr/bin/env python3
"""
Simple helper that converts any input string into a Code128 barcode image.

Requires:
    pip install python-barcode pillow
"""

from __future__ import annotations

import argparse
from pathlib import Path

from barcode import Code128
from barcode.writer import ImageWriter


def build_barcode(payload: str, output: Path) -> Path:
    """Render payload as Code128 PNG and return the path that was written."""
    barcode = Code128(
        payload,
        writer=ImageWriter(),
    )

    # png writer auto-adds .png if not present
    saved_path = Path(barcode.save(
        str(output.with_suffix("")),
        options={
            "module_width": 0.4,
            "module_height": 15.0,
            "font_size": 12,
            "text_distance": 8,
            "quiet_zone": 6,
        },
    ))
    return saved_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert an arbitrary string into a Code128 barcode image.",
    )
    parser.add_argument(
        "payload",
        nargs="?",
        help="text or numeric content that should be encoded (prompts if omitted)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("barcode.png"),
        help="target file (default: %(default)s)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    payload = args.payload or input("Text für den Barcode: ").strip()
    if not payload:
        raise SystemExit("Kein Text angegeben – Abbruch.")

    path = build_barcode(payload, args.output)
    print(f"Saved barcode to {path}")


if __name__ == "__main__":
    main()
