import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# --- Ubuntu 中文配置 ---
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False                 # 解决负号 '-' 显示为方块的问题

# 1. 准备数据
# ==========================================================
# 示例数据：你可以替换为你自己的 x 和 y 列表
x_data = np.array([30.0 , 35.0 , 40.0, 45.0, 50.60, 55.0, 60.0, 65.0])
# 假设 y_data 接近 y = 2x + 5，并加入一些随机噪声
y_data = np.array([56.45, 57.49, 58.56, 59.60, 60.70, 61.80, 62.80, 63.90])

# 2. 线性拟合
# ==========================================================
# 使用 scipy.stats.linregress 进行线性回归
# 它返回斜率 (slope)、截距 (intercept)、相关系数 (r_value) 等
slope, intercept, r_value, p_value, std_err = linregress(x_data, y_data)

# 构造拟合直线上的 y 值
y_fit = slope * x_data + intercept

# 3. 结果输出
# ==========================================================
print(f"线性拟合结果:")
print(f"  斜率 (Slope, m): {slope:.4f}")
print(f"  截距 (Intercept, c): {intercept:.4f}")
print(f"  相关系数 (R-value): {r_value:.4f}")
print(f"  拟合公式: y = {slope:.4f}x + {intercept:.4f}")
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

# 绘制拟合直线
plt.plot(x_data, y_fit, 
         label=f'拟合直线: y = {slope:.3f}x + {intercept:.3f}', 
         color='red', 
         linestyle='-', 
         linewidth=2)

# 添加散点图以突出原始数据点
plt.scatter(x_data, y_data, 
            
            color='blue', 
            marker='o')


# 添加标题和标签
#plt.title(r'作图法确定 $\alpha$ 测量结果', fontsize=16)
plt.xlabel(r'$t$ ($^{\circ}\mathrm{C}^{-1}$)', fontsize=14)
plt.ylabel(r'$R_t (\Omega)$', fontsize=14)
plt.legend(loc='best')
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()

# 保存图片
plt.savefig('linear_fit_chart.jpg', dpi=300, quality=90, optimize=True)

# 显示图形
plt.show()