# DIP Task2 — JPEG Compression & Channel Decomposition

A digital image processing tool that analyzes JPEG lossy compression by comparing quality levels, decomposing color channels (RGB/YUV), and measuring PSNR distortion.

## Requirements

- Python 3.8+
- OpenCV (`cv2`)
- NumPy
- Matplotlib

Install dependencies:

```bash
pip install opencv-python numpy matplotlib
```

## Usage

### Run the full pipeline

```bash
python main.py <image_path> [options]
```

**Positional arguments:**

| Argument | Description |
|----------|-------------|
| `image` | Path to the test image (default: `test.png`) |

**Options:**

| Option | Description |
|--------|-------------|
| `--quality 90 70 50 30 10` | Custom JPEG quality levels |
| `--no-psnr` | Skip PSNR comparison |

**Examples:**

```bash
# Use the default test.png
python main.py

# Specify a custom image
python main.py photo.jpg

# Custom quality levels, skip PSNR
python main.py photo.jpg --quality 100 80 50 20 5 --no-psnr
```

### Run PSNR comparison separately

```bash
python compare.py <image_path> [--quality 90 70 50 30 10]
```

## What It Does

### Task 1 — JPEG Compression Quality Analysis

Compresses the input image at multiple JPEG quality levels (default: 90, 70, 50, 30, 10) and plots the relationship between quality factor and output file size.

**Output:** `jpeg_quality_vs_size.png`

### Task 2 — Channel Decomposition

Takes the most compressed image (lowest quality) and decomposes it into:

- **RGB channels:** Red, Green, Blue
- **YUV channels:** Y (Luminance), U (Chrominance), V (Chrominance)

This reveals how JPEG compression affects luminance vs. chrominance differently — JPEG typically discards more chrominance data since the human eye is less sensitive to color detail.

**Output:** `channel_decomposition_comparison.png`

### Task 3 — PSNR Comparison

Calculates Peak Signal-to-Noise Ratio (PSNR) for Y, U, and V channels between the original and each compressed image. Higher PSNR = less distortion.

This step can be skipped with `--no-psnr`.

## Key Concepts

- **JPEG Compression:** Based on Discrete Cosine Transform (DCT) + quantization. The quality factor controls the quantization table — lower quality means larger quantization steps and more high-frequency coefficients zeroed out.
- **YUV Color Space:** Separates luminance (Y) from chrominance (U, V). JPEG exploits this by applying heavier compression to chrominance channels (chroma subsampling).
- **PSNR (Peak Signal-to-Noise Ratio):** Objective image quality metric. Values above 40 dB indicate excellent quality, 30–40 dB is acceptable, below 30 dB shows visible distortion.

## File Structure

```
task2/
├── main.py                     # Entry point with CLI argument parsing
├── jpeg_compression.py         # Task 1: JPEG quality vs size analysis
├── channel_decomposition.py    # Task 2: RGB/YUV channel visualization
├── compare.py                  # Task 3: PSNR comparison (also runnable standalone)
└── README.md
```
