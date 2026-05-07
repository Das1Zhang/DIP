import cv2
import os
import matplotlib.pyplot as plt


def lab_task_1_jpeg_compression(image_path):
    """
    任务 (1)：实现不同质量的图像JPEG压缩，观察质量与文件大小的关系
    """
    print("--- 任务 (1)：JPEG 压缩质量与文件大小关系 ---")

    if not os.path.exists(image_path):
        print(f"找不到图像文件: {image_path}，请修改路径。")
        return None

    img = cv2.imread(image_path)
    original_size = os.path.getsize(image_path)
    print(f"原始图像大小: {original_size / 1024:.2f} KB")

    quality_levels = [90, 70, 50, 30, 10]
    sizes = []
    saved_paths = []

    for q in quality_levels:
        # 设置JPEG压缩质量参数，设定压缩质量为 q
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), q]
        save_path = f"compressed_q{q}.jpg"
        cv2.imwrite(save_path, img, encode_param)
        saved_paths.append(save_path)
        file_size = os.path.getsize(save_path)
        sizes.append(file_size)
        print(f"质量因子: {q:2d} | 文件大小: {file_size / 1024:>6.2f} KB | 压缩率: {original_size/file_size:.2f}x")

    plt.figure(figsize=(8, 5))
    plt.plot(quality_levels, [s / 1024 for s in sizes], marker='o', linestyle='-', color='b')
    plt.title('JPEG Compression Quality vs File Size')
    plt.xlabel('Quality Factor (0-100)')
    plt.ylabel('File Size (KB)')
    plt.grid(True)
    plt.gca().invert_xaxis()

    plot_path = 'jpeg_quality_vs_size.png'
    plt.savefig(plot_path, bbox_inches='tight')
    print(f'已保存图像质量折线图: {plot_path}')
    plt.show()

    return saved_paths
