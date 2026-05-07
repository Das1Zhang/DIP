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

# --- 主程序运行示例 ---
# --- 主程序运行示例 ---
if __name__ == "__main__":
    # 1. 读取测试图像
    img = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE) 
    if img is None:
        print("错误：无法读取 test.png，请检查文件名和路径！")
        exit()

    height, width = img.shape
    max_display_size = 800 
    if width > max_display_size or height > max_display_size:
        scale = max_display_size / max(width, height)
        img = cv2.resize(img, (int(width * scale), int(height * scale)))

    # 2. 生成噪声与去噪图像
    img_gaussian = add_gaussian_noise(img, var=0.05)
    img_sp = add_salt_and_pepper_noise(img, amount=0.08)
    denoised_gaussian_mean = apply_mean_filter(img_gaussian, kernel_size=5)
    denoised_sp_median = apply_median_filter(img_sp, kernel_size=5)

    # 3. 绘制 5合1 图像
    plt.figure(figsize=(15, 8))
    plt.suptitle("Image Noise & Denoising Comparison", fontsize=16)

    plt.subplot(2, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title("1. Original Image")
    plt.axis('off') 

    plt.subplot(2, 3, 2)
    plt.imshow(img_gaussian, cmap='gray')
    plt.title("2. Gaussian Noise")
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.imshow(img_sp, cmap='gray')
    plt.title("3. Salt & Pepper Noise")
    plt.axis('off')

    plt.subplot(2, 3, 5)
    plt.imshow(denoised_gaussian_mean, cmap='gray')
    plt.title("4. Gaussian -> Mean Filter")
    plt.axis('off')

    plt.subplot(2, 3, 6)
    plt.imshow(denoised_sp_median, cmap='gray')
    plt.title("5. S&P -> Median Filter")
    plt.axis('off')

    plt.tight_layout()
    
    # ==========================================
    # 🌟 新增：保存 5合1 拼图到当前目录 (必须放在 show 之前)
    # ==========================================
    plt.savefig('noise_comparison_5in1.png', dpi=300, bbox_inches='tight')
    print("✅ 5合1对比图已保存为 'noise_comparison_5in1.png'")
    
    plt.show()

    # 4. 执行暗场噪声统计
    analyze_device_noise('black.png')