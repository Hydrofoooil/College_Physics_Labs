import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ================= 配置区 =================
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False                 # 解决负号 '-' 显示为方块的问题
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'

# ================= 数据准备 =================

# --- 数据集 1: 距离 L 与 饱和电流 iS ---
L_cm = np.array([40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30])
iS_dist = np.array([5.96, 6.31, 6.73, 7.44, 8.36, 8.93, 9.66, 10.35, 11.18, 12.40, 13.40])
# 转换 X 轴数据: 1/L^2 (单位 cm^-2)
X_dist = 1 / (L_cm ** 2)

# --- 数据集 2: 孔径 Phi 与 饱和电流 iS ---
Phi_mm = np.array([2, 4, 8])
iS_aper = np.array([6.20, 22.9, 86.7])
# 转换 X 轴数据: Phi^2 (单位 mm^2)
X_aper = Phi_mm ** 2

# ================= 绘图函数 =================
def plot_verification(x, y, xlabel, ylabel, title, filename, formula_fmt):
    plt.figure(figsize=(7, 5), dpi=300)
    
    # 线性拟合
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    line_x = np.linspace(0, x.max() * 1.1, 100)
    line_y = slope * line_x + intercept
    
    # 绘制散点和拟合线
    plt.scatter(x, y, color='black', marker='o', label='实验数据')
    plt.plot(line_x, line_y, color='red', linestyle='--', label=f'线性拟合 ($R^2={r_value**2:.4f}$)')
    
    # 辅助线 (过零点检查)
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    
    # 标注方程
    sign = "+" if intercept >= 0 else "-"
    eq_text = f"$y = {slope:.2f}x {sign} {abs(intercept):.2f}$"
    plt.text(0.05, 0.85, eq_text, transform=plt.gca().transAxes, 
             bbox=dict(boxstyle="round", fc="white", ec="gray"), fontsize=11)

    # 装饰
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.title(title, fontsize=13)
    plt.legend(loc='lower right')
    plt.grid(True, linestyle=':', alpha=0.6)
    
    # 强制从 0 开始显示，验证正比性
    plt.xlim(left=0)
    plt.ylim(bottom=0)
    
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Saved {filename}")

# ================= 生成图表 =================
# 1. 验证 iS 与 1/L^2 的关系
plot_verification(
    X_dist, iS_dist, 
    xlabel=r'距离平方倒数 $1/L^2$ ($\mathrm{cm}^{-2}$)', 
    ylabel=r'饱和电流 $i_S$ ($10^{-10}$ A)',
    title=r'验证饱和电流与光强关系 (改变距离)',
    filename='saturation_distance.png',
    formula_fmt=""
)

# 2. 验证 iS 与 Phi^2 的关系
# 修改点：将 \text{mm} 改为 \mathrm{mm}
plot_verification(
    X_aper, iS_aper,
    xlabel=r'孔径平方 $\Phi^2$ ($\mathrm{mm}^{2}$)',
    ylabel=r'饱和电流 $i_S$ ($10^{-10}$ A)',
    title=r'验证饱和电流与光强关系 (改变光阑)',
    filename='saturation_aperture.png',
    formula_fmt=""
)