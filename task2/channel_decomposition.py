import cv2
import matplotlib.pyplot as plt


def lab_task_2_channel_decomposition(compressed_image_path):
    """
    任务 (2)：将压缩图像在RGB和YUV通道进行分解，观察不同通道的压缩质量
    """
    print(f"\n--- 任务 (2)：通道分解 (使用严重压缩的图像: {compressed_image_path}) ---")

    img_bgr = cv2.imread(compressed_image_path)
    if img_bgr is None:
        print(f"找不到图像文件: {compressed_image_path}，请修改路径。")
        return

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)

    r, g, b = cv2.split(img_rgb)
    y, u, v = cv2.split(img_yuv)

    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    plt.suptitle(f"Channel Decomposition ({compressed_image_path})", fontsize=16)

    axes[0, 0].imshow(img_rgb)
    axes[0, 0].set_title("Compressed Image (RGB)")
    axes[0, 0].axis('off')

    axes[0, 1].imshow(r, cmap='gray')
    axes[0, 1].set_title("R Channel")
    axes[0, 1].axis('off')

    axes[0, 2].imshow(g, cmap='gray')
    axes[0, 2].set_title("G Channel")
    axes[0, 2].axis('off')

    axes[0, 3].imshow(b, cmap='gray')
    axes[0, 3].set_title("B Channel")
    axes[0, 3].axis('off')

    # 直接将 YUV 数组传给 imshow 颜色会失真，仅作原始数据占位展示
    axes[1, 0].imshow(img_yuv)
    axes[1, 0].set_title("Compressed Image (YUV Array)")
    axes[1, 0].axis('off')

    axes[1, 1].imshow(y, cmap='gray')
    axes[1, 1].set_title("Y (Luminance) Channel")
    axes[1, 1].axis('off')

    axes[1, 2].imshow(u, cmap='gray')
    axes[1, 2].set_title("U (Chrominance) Channel")
    axes[1, 2].axis('off')

    axes[1, 3].imshow(v, cmap='gray')
    axes[1, 3].set_title("V (Chrominance) Channel")
    axes[1, 3].axis('off')

    plt.tight_layout()
    plot_path = 'channel_decomposition_comparison.png'
    plt.savefig(plot_path, bbox_inches='tight')
    print(f'已保存通道分解对比图: {plot_path}')
    plt.show()
