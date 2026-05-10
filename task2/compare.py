import argparse
import os

import cv2
import numpy as np


def calculate_psnr(original, compressed):
    """Calculate PSNR between two single-channel images."""
    mse = np.mean((original.astype(np.float64) - compressed.astype(np.float64)) ** 2)
    if mse == 0:
        return float("inf")
    max_pixel = 255.0
    return 10 * np.log10((max_pixel ** 2) / mse)


def compare_yuv_quality(original_path, compressed_path):
    """Compare PSNR of Y, U, V channels between original and compressed images."""
    print(f"\n--- PSNR Comparison: {compressed_path} ---")

    img_orig = cv2.imread(original_path)
    img_comp = cv2.imread(compressed_path)

    if img_orig is None:
        print(f"  Error: cannot read {original_path}")
        return
    if img_comp is None:
        print(f"  Error: cannot read {compressed_path}")
        return

    img_orig_yuv = cv2.cvtColor(img_orig, cv2.COLOR_BGR2YUV)
    img_comp_yuv = cv2.cvtColor(img_comp, cv2.COLOR_BGR2YUV)

    y_orig, u_orig, v_orig = cv2.split(img_orig_yuv)
    y_comp, u_comp, v_comp = cv2.split(img_comp_yuv)

    psnr_y = calculate_psnr(y_orig, y_comp)
    psnr_u = calculate_psnr(u_orig, u_comp)
    psnr_v = calculate_psnr(v_orig, v_comp)

    print(f"  Y (Luminance)  PSNR: {psnr_y:.2f} dB")
    print(f"  U (Chrominance) PSNR: {psnr_u:.2f} dB")
    print(f"  V (Chrominance) PSNR: {psnr_v:.2f} dB")


def run_psnr_analysis(original_path, compressed_paths):
    """
    Run PSNR comparison on multiple compressed images against the original.

    Args:
        original_path: Path to the original image.
        compressed_paths: List of paths to compressed images.
    """
    print("\n--- Task 3: PSNR Channel Quality Comparison ---")
    for path in compressed_paths:
        if os.path.exists(path):
            compare_yuv_quality(original_path, path)
        else:
            print(f"  Skipping missing file: {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Compare PSNR between original and JPEG-compressed images"
    )
    parser.add_argument(
        "image",
        nargs="?",
        default="test.png",
        help="Path to the original image (default: test.png)",
    )
    parser.add_argument(
        "--quality",
        type=int,
        nargs="+",
        default=[90, 70, 50, 30, 10],
        help="Quality levels to compare (default: 90 70 50 30 10)",
    )
    args = parser.parse_args()

    if not os.path.exists(args.image):
        print(f"Error: image not found: {args.image}")
        exit(1)

    compressed_paths = [f"compressed_q{q}.jpg" for q in args.quality]
    run_psnr_analysis(args.image, compressed_paths)
