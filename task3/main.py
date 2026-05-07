# main.py
import os
# 从你保存的算法文件中导入 color_transfer 函数
# 假设你的算法文件名为 color_transfer_algo.py
from color_transfer_algo import color_transfer

def main():
    # 1. 设置图片的路径
    # 请确保这些图片在你运行代码的当前目录下，或者使用绝对路径
    target_image = "normal.png"  # 你的目标图像（需要被改变颜色的图）
    source_image = "forests.jpg"  # 你的源图像（提供色彩风格的图）
    output_image = "forest_result.jpg"  # 处理后生成的图像名称

    # 2. 简单的文件检查（防止找不到图片报错）
    if not os.path.exists(target_image):
        print(f"错误: 找不到目标图像 '{target_image}'")
        return
    if not os.path.exists(source_image):
        print(f"错误: 找不到源图像 '{source_image}'")
        return

    # 3. 调用色彩迁移函数
    print("开始进行色彩迁移，请稍候...")
    try:
        color_transfer(target_image, source_image, output_image)
        print(f"处理成功！结果已保存为: {output_image}")
    except Exception as e:
        print(f"处理过程中发生错误: {e}")

if __name__ == "__main__":
    main()