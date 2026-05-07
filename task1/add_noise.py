import cv2
import numpy as np

def add_gaussian_noise(image, mean=0, var=0.01):
    """添加高斯噪声,生成一个服从正态分布的随机矩阵，并将其叠加到原图上"""
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    return out

def add_salt_and_pepper_noise(image, amount=0.05, salt_vs_pepper=0.5):
    """添加椒盐噪声，将某些位置的像素改成极值"""
    row, col = image.shape[:2]
    out = np.copy(image)
    # 添加盐噪声 (Salt, 白色)
    num_salt = np.ceil(amount * image.size * salt_vs_pepper)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    out[tuple(coords)] = 255
    # 添加椒噪声 (Pepper, 黑色)
    num_pepper = np.ceil(amount * image.size * (1. - salt_vs_pepper))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    out[tuple(coords)] = 0
    return out

def apply_mean_filter(image, kernel_size=3):
    """均值滤波 (线性滤波)"""
    return cv2.blur(image, (kernel_size, kernel_size))

def apply_median_filter(image, kernel_size=3):
    """中值滤波 (统计/非线性滤波)"""
    return cv2.medianBlur(image, kernel_size)