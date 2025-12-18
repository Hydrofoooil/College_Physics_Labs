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
    -4.5, -3.5, -2.5, -1.5, -1.0, -0.8,
    -0.7, -0.6, -0.55, -0.5, -0.4, -0.2,
    0.0, 2.0, 6.0, 10.0, 15.0, 20.0, 25.0, 30.0
])

# 电流 I (A) 
# 将原来的科学计数法字符串转换为统一的数值
I = np.array([
    -117e-13, -110e-13, -103e-13, -94e-13, -86e-13, -77e-13,
    -71e-13,  -59e-13,  -34e-13,  53e-13,  520e-13, 192e-12,
    352e-12,  215e-11,  431e-11,  564e-11, 71e-10,  81e-10,  88e-10,  96e-10
])

# 为了绘图方便，将电流单位转换为纳安 (nA, 1e-9 A)
I_plot = I * 1e9 

# ================= 曲线拟合 (平滑插值) =================
# 使用 B-Spline 生成平滑曲线
# k=3 表示三次样条插值，曲线会非常圆滑
X_smooth = np.linspace(U.min(), U.max(), 300)
spl = make_interp_spline(U, I_plot, k=3) 
Y_smooth = spl(X_smooth)

# ================= 绘图 =================
plt.figure(figsize=(10, 6), dpi=300)

# 1. 绘制实验点
plt.scatter(U, I_plot, color='black', marker='o', s=40, label='实验数据点', zorder=5)

# 2. 绘制平滑曲线
plt.plot(X_smooth, Y_smooth, color='blue', linewidth=2, label='伏安特性曲线 (样条拟合)')

# 3. 辅助线 (零点)
plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
plt.axvline(0, color='gray', linestyle='--', linewidth=0.8)

# 4. 标注与装饰
plt.xlabel('电压 $U_{AK}$ (V)', fontsize=12)
plt.ylabel('光电流 $I$ ($10^{-9}$ A)', fontsize=12) # 注意单位变化
plt.title('577nm 单色光伏安特性曲线 ($I-U$)', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='lower right', fontsize=12)

# 添加箭头指示饱和区和截止区
plt.annotate('饱和电流区', xy=(25, 9), xytext=(20, 5),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
plt.annotate('截止区', xy=(-2, 0), xytext=(-4, 2),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()
plt.savefig('iv_curve_smooth.png')
print("图片已保存为 iv_curve_smooth.png")
# plt.show()