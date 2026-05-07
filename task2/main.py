from jpeg_compression import lab_task_1_jpeg_compression
from channel_decomposition import lab_task_2_channel_decomposition

if __name__ == "__main__":
    # 请确保同级目录下有一张名为 test.jpg 的图片
    test_image = "test.png"

    generated_files = lab_task_1_jpeg_compression(test_image)

    if generated_files:
        lab_task_2_channel_decomposition("compressed_q10.jpg")
