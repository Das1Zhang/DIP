import argparse
import os
import sys

from jpeg_compression import jpeg_compress_analysis
from channel_decomposition import channel_decomposition_visualize
from compare import run_psnr_analysis


def main():
    parser = argparse.ArgumentParser(
        description="JPEG compression quality analysis and channel decomposition tool"
    )
    parser.add_argument(
        "image",
        nargs="?",
        default="test.png",
        help="Path to the test image (default: test.png)",
    )
    parser.add_argument(
        "--no-psnr",
        action="store_true",
        help="Skip PSNR comparison analysis",
    )
    parser.add_argument(
        "--quality",
        type=int,
        nargs="+",
        default=[90, 70, 50, 30, 10],
        help="Quality levels for JPEG compression (default: 90 70 50 30 10)",
    )
    args = parser.parse_args()

    if not os.path.exists(args.image):
        print(f"Error: image file not found: {args.image}")
        sys.exit(1)

    print(f"Using test image: {args.image}")

    # Task 1: JPEG compression quality analysis
    saved_paths = jpeg_compress_analysis(args.image, args.quality)
    if not saved_paths:
        print("Error: JPEG compression failed.")
        sys.exit(1)

    # Task 2: Channel decomposition on the most compressed image
    channel_decomposition_visualize(saved_paths[-1])

    # Task 3: PSNR comparison
    if not args.no_psnr:
        run_psnr_analysis(args.image, saved_paths)


if __name__ == "__main__":
    main()
