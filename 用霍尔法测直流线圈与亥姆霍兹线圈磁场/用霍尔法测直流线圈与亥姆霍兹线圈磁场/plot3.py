import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False                 # 解决负号 '-' 显示为方块的问题

# 数据录入
Y_vals = np.array([-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
B_vals = np.array([1.207, 1.117, 1.060, 1.022, 1.006, 1.002, 1.014, 1.041, 1.095, 1.167, 1.291])

# 使用二次多项式拟合 (y = ax^2 + bx + c)
# 径向分布通常在近轴处近似为偶函数（抛物线）
coeffs = np.polyfit(Y_vals, B_vals, 2)
poly_func = np.poly1d(coeffs)

# 生成平滑曲线
Y_smooth = np.linspace(min(Y_vals), max(Y_vals), 300)
B_smooth = poly_func(Y_smooth)

# 绘图
plt.figure(figsize=(10, 6))
plt.scatter(Y_vals, B_vals, color='red', label='测量值 (mT)', zorder=5)
plt.plot(Y_smooth, B_smooth, color='blue', label='二次曲线拟合', linewidth=2)

# 设置标签和标题
plt.title('载流圆线圈中心平面内径向磁场分布', fontsize=14)
plt.xlabel(r'距中心距离 Y ($10^{-2}$ m)', fontsize=12)
plt.ylabel('磁感应强度 B (mT)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.axvline(x=0, color='gray', linestyle=':', alpha=0.5)

# 保存
plt.savefig('radial_distribution_fit.png')