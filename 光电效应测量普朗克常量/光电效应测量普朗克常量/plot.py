import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ================= 设置 =================
# 设置中文字体 (根据您的系统选择)

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False                 # 解决负号 '-' 显示为方块的问题

# ================= 数据 =================
# 波长 (nm) -> 频率 (Hz)
c = 2.99792458e8
lambdas = np.array([365, 405, 436, 546, 577])
nu = c / (lambdas * 1e-9) 

# 截止电压 (V) -> 取绝对值
U_a = np.abs(np.array([-1.720, -1.399, -1.184, -0.638, -0.532]))

# ================= 拟合 =================
slope, intercept, r_value, p_value, std_err = stats.linregress(nu, U_a)
fit_fn = np.poly1d([slope, intercept]) 

# ================= 绘图 =================
plt.figure(figsize=(8, 6), dpi=300)

# 1. 绘制实验点
plt.scatter(nu, U_a, color='black', marker='o', s=50, label='实验数据', zorder=5)

# 2. 绘制拟合线
x_range = np.linspace(nu.min()*0.9, nu.max()*1.05, 100)
plt.plot(x_range, fit_fn(x_range), 'r--', linewidth=1.5, label='线性拟合')

# 3. 标注
plt.xlabel(r'频率 $\nu$ ($\times 10^{14}$ Hz)', fontsize=12)
plt.ylabel(r'截止电压 $|U_a|$ (V)', fontsize=12)
plt.title(r'光电效应实验：截止电压与频率关系', fontsize=14)

# 坐标轴科学计数法显示优化
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

# 图例与网格
plt.legend(frameon=True, fontsize=11)
plt.grid(linestyle='--', alpha=0.5)

# 在图中显示拟合公式
eq_str = f'$U = {slope*1e15:.3f}\\times 10^{{-15}}\\nu {intercept:.3f}$\n$R^2 = {r_value**2:.4f}$'
plt.text(0.05, 0.85, eq_str, transform=plt.gca().transAxes, 
         fontsize=11, bbox=dict(boxstyle="round", fc="white", ec="gray", alpha=0.9))

# 保存图片
plt.tight_layout()
plt.savefig('photoelectric_fit.png')
print("图片已保存为 photoelectric_fit.png")
# plt.show()import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# ================= 数据 =================
# 波长 (nm) -> 频率 (Hz)
c = 2.99792458e8
lambdas = np.array([365, 405, 436, 546, 577])
nu = c / (lambdas * 1e-9) 

# 截止电压 (V) -> 取绝对值
U_a = np.abs(np.array([-1.720, -1.399, -1.184, -0.638, -0.532]))

# ================= 拟合 =================
slope, intercept, r_value, p_value, std_err = stats.linregress(nu, U_a)
fit_fn = np.poly1d([slope, intercept]) 

# ================= 绘图 =================
plt.figure(figsize=(8, 6), dpi=300)

# 1. 绘制实验点
plt.scatter(nu, U_a, color='black', marker='o', s=50, label='实验数据', zorder=5)

# 2. 绘制拟合线
x_range = np.linspace(nu.min()*0.9, nu.max()*1.05, 100)
plt.plot(x_range, fit_fn(x_range), 'r--', linewidth=1.5, label='线性拟合')

# 3. 标注
plt.xlabel(r'频率 $\nu$ ($\times 10^{14}$ Hz)', fontsize=12)
plt.ylabel(r'截止电压 $|U_a|$ (V)', fontsize=12)
plt.title(r'光电效应实验：截止电压与频率关系', fontsize=14)

# 坐标轴科学计数法显示优化
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

# 图例与网格
plt.legend(frameon=True, fontsize=11)
plt.grid(linestyle='--', alpha=0.5)

# 在图中显示拟合公式
eq_str = f'$U = {slope*1e15:.3f}\\times 10^{{-15}}\\nu {intercept:.3f}$\n$R^2 = {r_value**2:.4f}$'
plt.text(0.05, 0.85, eq_str, transform=plt.gca().transAxes, 
         fontsize=11, bbox=dict(boxstyle="round", fc="white", ec="gray", alpha=0.9))

# 保存图片
plt.tight_layout()
plt.savefig('photoelectric_fit.png')
print("图片已保存为 photoelectric_fit.png")
# plt.show()