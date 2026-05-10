# main.py
import argparse
import os
from color_transfer_algo import color_transfer


def main():
    parser = argparse.ArgumentParser(
        description="Reinhard 色彩迁移：将源图像的色彩风格迁移到目标图像上"
    )
    parser.add_argument("target", help="目标图像路径（需要被改变颜色的图）")
    parser.add_argument("source", help="源图像路径（提供色彩风格的图）")
    parser.add_argument(
        "-o", "--output",
        help="输出图像路径（默认: result.jpg）",
        default="result.jpg",
    )

    args = parser.parse_args()

    if not os.path.exists(args.target):
        print(f"错误: 找不到目标图像 '{args.target}'")
        return
    if not os.path.exists(args.source):
        print(f"错误: 找不到源图像 '{args.source}'")
        return

    print("开始进行色彩迁移，请稍候...")
    try:
        color_transfer(args.target, args.source, args.output)
        print(f"处理成功！结果已保存为: {args.output}")
    except Exception as e:
        print(f"处理过程中发生错误: {e}")


if __name__ == "__main__":
    main()
