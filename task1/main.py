import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt
from add_noise import (
    add_gaussian_noise,
    add_salt_and_pepper_noise,
    apply_mean_filter,
    apply_median_filter,
)
from analyze import analyze_device_noise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="图像噪声与去噪对比演示")
    parser.add_argument("image", nargs="?", default="test.png",
                        help="测试图像路径 (默认: test.png)")
    parser.add_argument("--black", default="black.png",
                        help="暗场图像路径 (默认: black.png)")
    parser.add_argument("--gaussian-var", type=float, default=0.05,
                        help="高斯噪声方差 (默认: 0.05)")
    parser.add_argument("--sp-amount", type=float, default=0.08,
                        help="椒盐噪声比例 (默认: 0.08)")
    parser.add_argument("--kernel-size", type=int, default=5,
                        help="滤波核大小，须为奇数 (默认: 5)")
    args = parser.parse_args()

    # 1. 读取测试图像
    img = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"错误：无法读取 '{args.image}'，请检查文件名和路径！")
        exit()

    height, width = img.shape
    max_display_size = 800
    if width > max_display_size or height > max_display_size:
        scale = max_display_size / max(width, height)
        img = cv2.resize(img, (int(width * scale), int(height * scale)))

    # 2. 生成噪声图像
    img_gaussian = add_gaussian_noise(img, var=args.gaussian_var)
    img_sp = add_salt_and_pepper_noise(img, amount=args.sp_amount)

    # 3. 对两张噪声图像分别使用均值滤波和中值滤波
    ksize = args.kernel_size
    gaussian_mean = apply_mean_filter(img_gaussian, kernel_size=ksize)
    gaussian_median = apply_median_filter(img_gaussian, kernel_size=ksize)
    sp_mean = apply_mean_filter(img_sp, kernel_size=ksize)
    sp_median = apply_median_filter(img_sp, kernel_size=ksize)

    # 4. 绘制 7合1 图像 (3x3 网格)
    plt.figure(figsize=(16, 10))
    plt.suptitle("Image Noise & Denoising Comparison (7 in 1)", fontsize=16, fontweight='bold')

    images = [
        ("Original Image", img),
        ("Gaussian Noise", img_gaussian),
        ("Salt & Pepper Noise", img_sp),
        ("Gaussian + Mean Filter", gaussian_mean),
        ("Gaussian + Median Filter", gaussian_median),
        ("S&P + Mean Filter", sp_mean),
        ("S&P + Median Filter", sp_median),
    ]

    for idx, (title, image) in enumerate(images):
        ax = plt.subplot(3, 3, idx + 1)
        ax.imshow(image, cmap='gray')
        ax.set_title(title, fontsize=11)
        ax.axis('off')

    plt.tight_layout()
    plt.savefig('noise_comparison_7in1.png', dpi=300, bbox_inches='tight')
    print("7合1对比图已保存为 'noise_comparison_7in1.png'")

    plt.show()

    # 5. 执行暗场噪声统计
    analyze_device_noise(args.black)