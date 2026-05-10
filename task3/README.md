# Color Transfer 色彩迁移

基于 Reinhard 等人《Color Transfer between Images》(2001) 论文实现的色彩迁移算法。将源图像的色彩风格迁移到目标图像上，保留目标图内容的同时赋予其源图的色调特征。

## 安装依赖

```bash
pip install opencv-python numpy
```

## 使用方法

```bash
python main.py <目标图像> <源图像> [-o 输出路径]
```

| 参数 | 说明 |
|------|------|
| `target` | 目标图像（需要被改变颜色的图） |
| `source` | 源图像（提供色彩风格的图） |
| `-o, --output` | 输出路径（默认: `result.jpg`） |

### 示例

```bash
# 将 forests.jpg 的色彩风格迁移到 normal.png 上
python main.py normal.png forests.jpg -o forest_result.jpg

# 将 sunset.jpg 的色彩风格迁移到 normal.png 上
python main.py normal.png sunset.jpg -o sunset_result.jpg
```

## 算法原理

Reinhard 色彩迁移的核心步骤：

1. **RGB → LMS**：转换到人眼锥体细胞响应空间
2. **LMS → log(LMS)**：取对数模拟非线性感知，降低通道相关性
3. **log(LMS) → lαβ**：转换到 Ruderman 感知颜色空间，三个通道在统计上几乎独立
4. **统计匹配**：将目标图像各通道的均值和标准差对齐到源图像
5. **逆变换(lαβ → LMS → RGB)**：转换回 RGB 并保存

```
目标图 RGB → LMS → Log → lαβ ───→ 统计匹配 ───→ lαβ' → 10^ → LMS → RGB → 结果
                                    ↑
源图像 RGB → LMS → Log → lαβ ───→ 计算 stats(μ, σ)
```

## 文件结构

```
task3/
├── main.py                   # 程序入口（命令行参数解析）
├── color_transfer_algo.py    # 核心算法实现
├── normal.png                # 目标图像示例
├── forests.jpg               # 源图像示例（森林色调）
├── sunset.jpg                # 源图像示例（日落色调）
└── README.md
```
