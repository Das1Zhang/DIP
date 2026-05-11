import cv2
import matplotlib.pyplot as plt


def _load_and_decompose(image_path):
    """Load an image and return its RGB, YUV arrays and split channels."""
    img_bgr = cv2.imread(image_path)
    if img_bgr is None:
        return None
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)
    r, g, b = cv2.split(img_rgb)
    y, u, v = cv2.split(img_yuv)
    return img_rgb, img_yuv, (r, g, b), (y, u, v)


def _draw_channel_row(axes, row_idx, full_img, ch1, ch2, ch3, label, ch_names):
    """Draw one row: full image + 3 single channels."""
    axes[row_idx, 0].imshow(full_img)
    axes[row_idx, 0].set_title(f"{label}")
    axes[row_idx, 0].axis("off")

    axes[row_idx, 1].imshow(ch1, cmap="gray")
    axes[row_idx, 1].set_title(f"{label} {ch_names[0]}")
    axes[row_idx, 1].axis("off")

    axes[row_idx, 2].imshow(ch2, cmap="gray")
    axes[row_idx, 2].set_title(f"{label} {ch_names[1]}")
    axes[row_idx, 2].axis("off")

    axes[row_idx, 3].imshow(ch3, cmap="gray")
    axes[row_idx, 3].set_title(f"{label} {ch_names[2]}")
    axes[row_idx, 3].axis("off")


def channel_decomposition_visualize(original_image_path, compressed_image_path):
    """
    Decompose both original and compressed images into RGB and YUV channels
    for side-by-side comparison.

    Args:
        original_image_path: Path to the original uncompressed image.
        compressed_image_path: Path to the compressed JPEG image.
    """
    print(f"\n--- Task 2: Channel Decomposition ---")
    print(f"  Original:   {original_image_path}")
    print(f"  Compressed: {compressed_image_path}")

    orig = _load_and_decompose(original_image_path)
    comp = _load_and_decompose(compressed_image_path)

    if orig is None:
        print(f"Image not found: {original_image_path}")
        return
    if comp is None:
        print(f"Image not found: {compressed_image_path}")
        return

    img_rgb_o, img_yuv_o, (r_o, g_o, b_o), (y_o, u_o, v_o) = orig
    img_rgb_c, img_yuv_c, (r_c, g_c, b_c), (y_c, u_c, v_c) = comp

    fig, axes = plt.subplots(4, 4, figsize=(16, 16))
    plt.suptitle("Channel Decomposition — Original vs Compressed", fontsize=16, y=0.98)

    # Row 0: Original RGB channels
    _draw_channel_row(axes, 0, img_rgb_o, r_o, g_o, b_o, "Original RGB", ("R", "G", "B"))
    # Row 1: Original YUV channels
    _draw_channel_row(axes, 1, img_rgb_o, y_o, u_o, v_o, "Original YUV", ("Y", "U", "V"))
    # Row 2: Compressed RGB channels
    _draw_channel_row(axes, 2, img_rgb_c, r_c, g_c, b_c, "Compressed RGB", ("R", "G", "B"))
    # Row 3: Compressed YUV channels
    _draw_channel_row(axes, 3, img_rgb_c, y_c, u_c, v_c, "Compressed YUV", ("Y", "U", "V"))

    plt.tight_layout()
    plot_path = "channel_decomposition_comparison.png"
    plt.savefig(plot_path, bbox_inches="tight")
    print(f"Saved channel decomposition plot: {plot_path}")
    plt.show()
