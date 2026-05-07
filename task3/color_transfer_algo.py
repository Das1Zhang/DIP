import cv2
import numpy as np

def color_transfer(target_path, source_path, output_path):
    """
    实现 Reinhard 等人的 Color Transfer 算法
    target_path: 内容图像（要改变色彩的图像）
    source_path: 风格图像（提供色彩的图像）
    """
    # 1. 读取图像并将 BGR 转换为 RGB
    target = cv2.imread(target_path)
    source = cv2.imread(source_path)
    target = cv2.cvtColor(target, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
    source = cv2.cvtColor(source, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0

    # 论文中提供的转换矩阵
    # RGB to LMS 
    M_RGB_to_LMS = np.array([
        [0.3811, 0.5783, 0.0402],
        [0.1967, 0.7244, 0.0782],
        [0.0241, 0.1288, 0.8444]
    ])

    # LMS to lab 的两步矩阵
    M_LMS_to_lab_1 = np.array([
        [1/np.sqrt(3), 0, 0],
        [0, 1/np.sqrt(6), 0],
        [0, 0, 1/np.sqrt(2)]
    ])
    M_LMS_to_lab_2 = np.array([
        [1, 1, 1],
        [1, 1, -2],
        [1, -1, 0]
    ])
    M_LMS_to_lab = np.dot(M_LMS_to_lab_1, M_LMS_to_lab_2)

    # lab to LMS [cite: 88-100]
    M_lab_to_LMS = np.array([
        [np.sqrt(3)/3, np.sqrt(6)/6, np.sqrt(2)/2],
        [np.sqrt(3)/3, np.sqrt(6)/6, -np.sqrt(2)/2],
        [np.sqrt(3)/3, -np.sqrt(6)/3, 0]
    ])

    # LMS to RGB [cite: 115-117]
    M_LMS_to_RGB = np.array([
        [4.4679, -3.5873, 0.1193],
        [-1.2186, 2.3809, -0.1624],
        [0.0497, -0.2439, 1.2045]
    ])

    def rgb_to_lab(img):
        # Flatten image to N x 3
        pixels = img.reshape(-1, 3)
        # Step 1: RGB to LMS
        lms = np.dot(pixels, M_RGB_to_LMS.T)
        # Step 2: 转换为对数空间 (Log base 10) 防止 log(0) 增加小偏置 [cite: 56-59, 114]
        lms_log = np.log10(np.clip(lms, 1e-6, None))
        # Step 3: LMS to lab
        lab = np.dot(lms_log, M_LMS_to_lab.T)
        return lab.reshape(img.shape)

    def lab_to_rgb(img_lab):
        pixels = img_lab.reshape(-1, 3)
        # Step 1: lab to LMS_log
        lms_log = np.dot(pixels, M_lab_to_LMS.T)
        # Step 2: 恢复线性空间 (10 的次幂) [cite: 114]
        lms = np.power(10, lms_log)
        # Step 3: LMS to RGB
        rgb = np.dot(lms, M_LMS_to_RGB.T)
        return rgb.reshape(img_lab.shape)

    def get_stats(img_lab):
        means = np.mean(img_lab, axis=(0, 1))
        stds = np.std(img_lab, axis=(0, 1))
        return means, stds

    # 执行空间转换
    target_lab = rgb_to_lab(target)
    source_lab = rgb_to_lab(source)

    # 获取统计信息 [cite: 125, 126]
    target_means, target_stds = get_stats(target_lab)
    source_means, source_stds = get_stats(source_lab)

    # 色彩迁移核心计算 [cite: 127-136]
    result_lab = np.zeros_like(target_lab)
    for i in range(3):
        # 减去目标均值，乘以标准差比例，加上源均值
        result_lab[:, :, i] = ((target_lab[:, :, i] - target_means[i]) * (source_stds[i] / target_stds[i])) + source_means[i]

    # 转换回 RGB 并处理越界值
    result_rgb = lab_to_rgb(result_lab)
    result_rgb = np.clip(result_rgb, 0.0, 1.0)
    
    # 转换回 BGR 保存
    result_bgr = cv2.cvtColor((result_rgb * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, result_bgr)
    print(f"Color transfer complete. Saved to {output_path}")

# 使用示例：
# color_transfer("target.jpg", "source.jpg", "output.jpg")