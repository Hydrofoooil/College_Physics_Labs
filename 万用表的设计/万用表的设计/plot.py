import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.optimize import curve_fit

# --- Ubuntu 中文配置 ---
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False                 # 解决负号 '-' 显示为方块的问题

# 1. 准备数据
# ==========================================================
# 示例数据：你可以替换为你自己的 x 和 y 列表
x_data = np.array([5.00, 4.50, 4.00, 3.50, 3.00, 2.50, 2.00, 1.50, 1.00, 0.50, 0.00])
# 假设 y_data 接近 y = 2x + 5，并加入一些随机噪声
y_data = np.array([0, 31.9 ,82.9 ,144.8, 223.1, 327.8 ,478.6 ,735.0, 1257.2 ,2810.1, np.inf ])
# 欧姆表数据：电流 Ix 与电阻 Rx
x_data_raw = np.array([5.00, 4.50, 4.00, 3.50, 3.00, 2.50, 2.00, 1.50, 1.00, 0.50, 0.00])
y_data_raw = np.array([0, 31.9, 82.9, 144.8, 223.1, 327.8, 478.6, 735.0, 1257.2, 2810.1, np.inf])

# 2. 线性拟合
# 过滤掉无穷大和零的值，避免拟合和除零错误
valid_indices = np.isfinite(y_data_raw) & (x_data_raw > 0)
x_data = x_data_raw[valid_indices]
y_data = y_data_raw[valid_indices]

# 2. 非线性拟合
# ==========================================================
# 使用 scipy.stats.linregress 进行线性回归
# 它返回斜率 (slope)、截距 (intercept)、相关系数 (r_value) 等
slope, intercept, r_value, p_value, std_err = linregress(x_data, y_data)
# 定义拟合函数模型，根据理论 R_x = epsilon / I_x - R_0
def fit_function(ix, epsilon, r0):
    return epsilon / ix - r0

# 构造拟合直线上的 y 值
y_fit = slope * x_data + intercept
# 使用 curve_fit 进行非线性拟合
# popt 是拟合出的最佳参数 [epsilon, r0]
# pcov 是参数的协方差矩阵
popt, pcov = curve_fit(fit_function, x_data, y_data)

# 提取拟合参数
epsilon_fit, r0_fit = popt

# 生成更平滑的x轴数据用于绘制拟合曲线
x_fit_smooth = np.linspace(min(x_data), max(x_data), 200)
y_fit_smooth = fit_function(x_fit_smooth, epsilon_fit, r0_fit)

# 3. 结果输出
# ==========================================================
print(f"线性拟合结果:")
print(f"  斜率 (Slope, m): {slope:.3e}")
print(f"  截距 (Intercept, c): {intercept:.3e}")
print(f"  相关系数 (R-value): {r_value:.4f}")
print(f"  拟合公式: y = {slope:.4f}x + {intercept:.4f}")
print(f"非线性拟合结果 (模型: R_x = epsilon / I_x - R_0):")
print(f"  拟合参数 epsilon: {epsilon_fit:.4f}")
print(f"  拟合参数 R_0: {r0_fit:.4f}")
print(f"  拟合公式: R_x = {epsilon_fit:.4f} / I_x - {r0_fit:.4f}")
print("-" * 30)

# 4. 绘图
# ==========================================================
plt.figure(figsize=(10, 6))

# 绘制原始数据的折线图
plt.plot(x_data, y_data, 
         label='实验数据点', 
         color='blue', 
         linestyle='--', 
         marker='o', 
         alpha=0.6)
# 绘制原始数据点
plt.scatter(x_data, y_data, label='实验数据点', color='blue', marker='o')

# 绘制拟合直线
plt.plot(x_data, y_fit, 
         label=f'拟合直线: y = {slope:.3e}x + {intercept:.3e}', 
         color='red', 
         linestyle='-', 
# 绘制拟合曲线
plt.plot(x_fit_smooth, y_fit_smooth,
         label=f'拟合曲线: $R_x = {epsilon_fit:.2f} / I_x - {r0_fit:.2f}$',
         color='red',
         linestyle='-',
         linewidth=2)

# 添加散点图以突出原始数据点
plt.scatter(x_data, y_data, 
            
            color='blue', 
            marker='o')


# 添加标题和标签
#plt.title(r'作图法确定 $\alpha$ 测量结果', fontsize=16)
plt.xlabel(r'$ I_B (mA)$', fontsize=14)
plt.ylabel(r'$ I_G (mA)$', fontsize=14)
plt.title('欧姆表刻度非线性关系拟合', fontsize=16)
plt.xlabel(r'电流 $I_x$ (mA)', fontsize=14)
plt.ylabel(r'电阻 $R_x$ ($\Omega$)', fontsize=14)
plt.legend(loc='best')
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()

# 保存图片
plt.savefig('linear_fit_chart.jpg', dpi=300, quality=90, optimize=True)
plt.savefig('nonlinear_fit_chart.jpg', dpi=300)

# 显示图形
plt.show()