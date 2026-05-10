import os

import cv2
import matplotlib.pyplot as plt


def jpeg_compress_analysis(image_path, quality_levels=None):
    """
    Compress an image at different JPEG quality levels and plot quality vs file size.

    Args:
        image_path: Path to the input image.
        quality_levels: List of quality factors (0-100). Defaults to [90, 70, 50, 30, 10].

    Returns:
        List of paths to the compressed images, or None on error.
    """
    if quality_levels is None:
        quality_levels = [90, 70, 50, 30, 10]

    print("--- Task 1: JPEG Compression Quality vs File Size ---")

    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        return None

    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to read image: {image_path}")
        return None

    original_size = os.path.getsize(image_path)
    print(f"Original image size: {original_size / 1024:.2f} KB")

    sizes = []
    saved_paths = []

    for q in quality_levels:
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), q]
        save_path = f"compressed_q{q}.jpg"
        cv2.imwrite(save_path, img, encode_param)
        saved_paths.append(save_path)
        file_size = os.path.getsize(save_path)
        sizes.append(file_size)
        print(f"  Quality: {q:2d} | Size: {file_size / 1024:>7.2f} KB | "
              f"Ratio: {original_size / file_size:.2f}x")

    plt.figure(figsize=(8, 5))
    plt.plot(quality_levels, [s / 1024 for s in sizes], marker="o", linestyle="-", color="b")
    plt.title("JPEG Compression Quality vs File Size")
    plt.xlabel("Quality Factor (0-100)")
    plt.ylabel("File Size (KB)")
    plt.grid(True)
    plt.gca().invert_xaxis()

    plot_path = "jpeg_quality_vs_size.png"
    plt.savefig(plot_path, bbox_inches="tight")
    print(f"Saved quality-vs-size plot: {plot_path}")
    plt.show()

    return saved_paths
