import matplotlib.pyplot as plt
import numpy as np
# --- Ubuntu 中文配置 ---
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False                 # 解决负号 '-' 显示为方块的问题

# 数据录入
X = [-10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
B_measured = [0.358, 0.417, 0.480, 0.557, 0.638, 0.725, 0.811, 0.885, 0.938, 0.984, 1.005, 0.984, 0.958, 0.895, 0.815, 0.734, 0.651, 0.566, 0.492, 0.428, 0.382]
B_theoretical = [0.355, 0.413, 0.479, 0.553, 0.634, 0.719, 0.805, 0.883, 0.948, 0.990, 1.005, 0.990, 0.948, 0.883, 0.805, 0.719, 0.634, 0.553, 0.479, 0.413, 0.355]

# 设置绘图风格
plt.figure(figsize=(10, 6))

# 绘制实验测量点
plt.scatter(X, B_measured, color='red', label='测量值 (mT)', marker='o', s=40, zorder=5)

# 绘制理论曲线
plt.plot(X, B_theoretical, color='blue', label='理论值 (mT)', linestyle='-', linewidth=2, alpha=0.7)

# 添加网格、标题和标签
plt.grid(True, linestyle='--', alpha=0.6)
plt.title('载流圆单线圈轴线上磁场分布', fontsize=14)
plt.xlabel(r'距离中心距离 X ($10^{-2}$ m)', fontsize=12)
plt.ylabel('磁感应强度 B (mT)', fontsize=12)
plt.legend()

# 标记中心位置
plt.axvline(x=0, color='gray', linestyle=':', alpha=0.5)

# 保存图片
plt.savefig('magnetic_field_distribution.png')