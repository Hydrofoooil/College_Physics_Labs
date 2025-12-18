import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# ================= 配置区 =================
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False                 # 解决负号 '-' 显示为方块的问题
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

# ================= 数据录入 =================
# 电压 U (V)
U = np.array([
    -4.5, -3.5, -2.5, -1.5, 0.0, 1.0, 
    1.3, 1.35, 1.4, 1.45, 1.5, 1.6, 
    2.0, 2.5, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0
])

# 电流 I (A) - 原始数据录入
# 修正了 2.5V 处的笔误: 284 -> 264 (参考原始图片)
I_raw = np.array([
    -118e-13, -108e-13, -95e-13, -60e-13, 593e-12, 130e-11,
    154e-11, 158e-11, 161e-11, 165e-11, 168e-11, 181e-11,
    215e-11, 264e-11, 478e-11, 68e-10, 93e-10, 117e-10, 136e-10, 148e-10
])

# 为了绘图清晰，将电流单位转换为 10^-9 A (nA)
I_plot = I_raw * 1e9 

# ================= 曲线拟合 (平滑插值) =================
# 使用 B-Spline 生成平滑曲线
# k=3 表示三次样条插值
# 由于数据点在 0-2V 之间很密集，插值效果通常很好
X_smooth = np.linspace(U.min(), U.max(), 500)
spl = make_interp_spline(U, I_plot, k=3) 
Y_smooth = spl(X_smooth)

# ================= 绘图 =================
plt.figure(figsize=(10, 6), dpi=300)

# 1. 绘制实验点
plt.scatter(U, I_plot, color='black', marker='o', s=40, label='实验数据点', zorder=5)

# 2. 绘制平滑曲线
plt.plot(X_smooth, Y_smooth, color='purple', linewidth=2, label='伏安特性曲线 (405nm)')

# 3. 辅助线 (零点)
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8)

# 4. 标注与装饰
plt.xlabel('电压 $U_{AK}$ (V)', fontsize=12)
plt.ylabel('光电流 $I$ ($10^{-9}$ A)', fontsize=12)
plt.title('405nm 单色光伏安特性曲线 ($I-U$)', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='lower right', fontsize=12)

# 标注截止电压位置 (近似)
# 405nm 截止电压理论值约为 -1.4V 左右，图中应该能看到曲线在 -1.5V 附近穿过零点
plt.annotate('截止电压 $U_a$', xy=(-1.4, 0), xytext=(-4, 2),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()
plt.savefig('iv_curve_405_smooth.png')
print("图片已保存为 iv_curve_405_smooth.png")
# plt.show()