import cv2
import matplotlib.pyplot as plt
def analyze_device_noise(image_path):
    """分析设备噪声并保存直方图"""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("未找到暗场图像，请检查路径。")
        return

    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    
    plt.figure(figsize=(10, 5))
    plt.title("Device Sensor Noise Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.plot(hist, color='black')
    
    # 你的图显示噪声主要集中在 0-50 之间，缩小X轴范围能看得更清楚
    plt.xlim([0, 50]) 
    plt.grid(alpha=0.3)
    
    # ==========================================
    # 🌟 新增：保存直方图到当前目录 (必须放在 show 之前)
    # bbox_inches='tight' 可以去除图片边缘多余的白边，dpi=300 保证高清
    # ==========================================
    plt.savefig('sensor_noise_histogram.png', dpi=300, bbox_inches='tight')
    print("✅ 直方图已保存为 'sensor_noise_histogram.png'")
    
    plt.show()