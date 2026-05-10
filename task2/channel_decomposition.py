import cv2
import matplotlib.pyplot as plt


def channel_decomposition_visualize(compressed_image_path):
    """
    Decompose a compressed image into RGB and YUV channels for visual comparison.

    Args:
        compressed_image_path: Path to the compressed JPEG image.
    """
    print(f"\n--- Task 2: Channel Decomposition ({compressed_image_path}) ---")

    img_bgr = cv2.imread(compressed_image_path)
    if img_bgr is None:
        print(f"Image not found: {compressed_image_path}")
        return

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)

    r, g, b = cv2.split(img_rgb)
    y, u, v = cv2.split(img_yuv)

    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    plt.suptitle(f"Channel Decomposition ({compressed_image_path})", fontsize=16)

    axes[0, 0].imshow(img_rgb)
    axes[0, 0].set_title("Compressed Image (RGB)")
    axes[0, 0].axis("off")

    axes[0, 1].imshow(r, cmap="gray")
    axes[0, 1].set_title("R Channel")
    axes[0, 1].axis("off")

    axes[0, 2].imshow(g, cmap="gray")
    axes[0, 2].set_title("G Channel")
    axes[0, 2].axis("off")

    axes[0, 3].imshow(b, cmap="gray")
    axes[0, 3].set_title("B Channel")
    axes[0, 3].axis("off")

    # YUV array displayed as-is will show distorted colors; kept as a data placeholder
    axes[1, 0].imshow(img_yuv)
    axes[1, 0].set_title("Compressed Image (YUV Array)")
    axes[1, 0].axis("off")

    axes[1, 1].imshow(y, cmap="gray")
    axes[1, 1].set_title("Y (Luminance) Channel")
    axes[1, 1].axis("off")

    axes[1, 2].imshow(u, cmap="gray")
    axes[1, 2].set_title("U (Chrominance) Channel")
    axes[1, 2].axis("off")

    axes[1, 3].imshow(v, cmap="gray")
    axes[1, 3].set_title("V (Chrominance) Channel")
    axes[1, 3].axis("off")

    plt.tight_layout()
    plot_path = "channel_decomposition_comparison.png"
    plt.savefig(plot_path, bbox_inches="tight")
    print(f"Saved channel decomposition plot: {plot_path}")
    plt.show()
