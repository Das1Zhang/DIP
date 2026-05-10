# Task 1 — 图像噪声与去噪对比

数字图像处理实验：对测试图像添加高斯噪声和椒盐噪声，然后分别用均值滤波和中值滤波进行交叉去噪，同时包含设备暗场噪声分析。

## 项目结构

```
task1/
├── main.py            # 主程序入口
├── add_noise.py       # 噪声生成与滤波算法
├── analyze.py         # 暗场噪声直方图分析
├── requirements.txt   # 依赖清单
├── test.png           # 测试图像（需自行准备）
├── black.png          # 暗场图像（需自行准备）
├── 核心代码解释.md     # 核心代码详细文档
├── noise_comparison_7in1.png   # 输出：7合1对比图
└── sensor_noise_histogram.png  # 输出：暗场噪声直方图
```

## 环境配置

```bash
pip install -r requirements.txt
```

依赖：`opencv-python >= 4.6.0`, `numpy >= 1.21.0`, `matplotlib >= 3.5.0`

## 使用方法

```bash
# 使用默认参数（读取 test.png 和 black.png）
python main.py

# 指定自定义测试图像
python main.py my_photo.jpg

# 完整自定义参数
python main.py photo.png --black dark.png --gaussian-var 0.03 --sp-amount 0.1 --kernel-size 3
```

### 命令行参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `image` | str | `test.png` | 测试图像路径（位置参数） |
| `--black` | str | `black.png` | 暗场图像路径 |
| `--gaussian-var` | float | `0.05` | 高斯噪声方差 |
| `--sp-amount` | float | `0.08` | 椒盐噪声比例 |
| `--kernel-size` | int | `5` | 滤波核大小（须为奇数） |

## 功能说明

### 1. 噪声生成 (`add_noise.py`)

| 函数 | 说明 |
|------|------|
| `add_gaussian_noise(image, mean, var)` | 添加高斯噪声（正态分布随机噪声） |
| `add_salt_and_pepper_noise(image, amount, salt_vs_pepper)` | 添加椒盐噪声（随机极值噪声） |

### 2. 去噪滤波 (`add_noise.py`)

| 函数 | 类型 | 擅长处理的噪声 |
|------|------|---------------|
| `apply_mean_filter(image, kernel_size)` | 线性滤波（均值） | 高斯噪声 |
| `apply_median_filter(image, kernel_size)` | 非线性滤波（中值） | 椒盐噪声 |

### 3. 暗场分析 (`analyze.py`)

读取暗场图像（无光照条件下拍摄），绘制像素强度直方图，用于评估设备传感器的本底噪声水平。

### 4. 输出

程序运行为每张噪声图像**交叉使用两种滤波**，生成 7 张图并合成一张：

- **第 1 行**：原图 → 高斯噪声 → 椒盐噪声
- **第 2 行**：高斯+均值滤波 → 高斯+中值滤波 → 椒盐+均值滤波
- **第 3 行**：椒盐+中值滤波

同时输出：
- `noise_comparison_7in1.png` — 7合1对比图
- `sensor_noise_histogram.png` — 暗场噪声直方图

## 算法原理简析

**高斯噪声**：噪声值服从正态分布，叠加到每个像素上，模拟传感器热噪声。

**椒盐噪声**：随机将某些像素强制置为 0（黑/椒）或 255（白/盐），模拟传输过程中的像素损坏。

**均值滤波**：取邻域像素的算术平均，能有效平滑高斯噪声（零均值噪声在平均后抵消），但对椒盐噪声无效（极值污染整个邻域）。

**中值滤波**：取邻域像素的中位数，对椒盐噪声效果极佳（孤立极值排到两端不影响中位数），且边缘保持能力优于均值滤波。
