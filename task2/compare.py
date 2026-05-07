import cv2
import numpy as np
import os
def calculate_psnr(original, compressed):
    """计算单通道图像的 PSNR 值"""
    # 计算均方误差 (MSE)
    mse = np.mean((original.astype(np.float64) - compressed.astype(np.float64)) ** 2)
    if mse == 0:
        return float('inf') # 如果完全一样，PSNR无穷大
    
    # 计算峰值信噪比 (PSNR)
    max_pixel = 255.0
    psnr = 10 * np.log10((max_pixel ** 2) / mse)
    return psnr

def compare_yuv_quality(original_path, compressed_path):
    """比较原始图像和压缩图像在 Y、U、V 三个通道上的 PSNR"""
    print(f"\n--- 比较原图与 {compressed_path} 的通道质量 ---")
    
    # 1. 读取原图和压缩图
    img_orig = cv2.imread(original_path)
    img_comp = cv2.imread(compressed_path)
    
    if img_orig is None or img_comp is None:
        print("错误：无法读取图片，请检查路径。")
        return

    # 2. 转换到 YUV 颜色空间
    img_orig_yuv = cv2.cvtColor(img_orig, cv2.COLOR_BGR2YUV)
    img_comp_yuv = cv2.cvtColor(img_comp, cv2.COLOR_BGR2YUV)

    # 3. 分离通道
    y_orig, u_orig, v_orig = cv2.split(img_orig_yuv)
    y_comp, u_comp, v_comp = cv2.split(img_comp_yuv)

    # 4. 计算并打印各个通道的 PSNR
    psnr_y = calculate_psnr(y_orig, y_comp)
    psnr_u = calculate_psnr(u_orig, u_comp)
    psnr_v = calculate_psnr(v_orig, v_comp)

    print(f"Y (亮度) 通道 PSNR : {psnr_y:.2f} dB")
    print(f"U (色度) 通道 PSNR : {psnr_u:.2f} dB")
    print(f"V (色度) 通道 PSNR : {psnr_v:.2f} dB")

test_image = "test.png" 
quality_levels = [90, 70, 50, 30, 10]
for q in quality_levels:    
    compressed_path = f"compressed_q{q}.jpg"
    if os.path.exists(compressed_path):
        compare_yuv_quality(test_image, compressed_path)