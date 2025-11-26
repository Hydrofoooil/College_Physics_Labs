import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False                 # 解决负号 '-' 显示为方块的问题

# 录入原始数据
X_vals = np.array([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
B_pos = np.array([837, 926, 1053, 1163, 1249, 1318, 1369, 1397, 1412, 1419, 1418, 1412, 1408, 1396, 1381, 1337, 1275, 1192, 1089, 983, 872])
B_neg = np.array([-887, -977, -1101, -1209, -1297, -1366, -1415, -1442, -1460, -1464, -1469, -1462, -1458, -1448, -1432, -1384, -1326, -1241, -1144, -1044, -937])

# 计算实测磁感应强度 (mT) = (|B+| + |B-|)/2 / 1000
B_measured = (np.abs(B_pos) + np.abs(B_neg)) / 2 / 1000

# 定义亥姆霍兹线圈的理论磁场公式 (设半径 R=10cm)
def helmholtz_field(x, C):
    R = 10.0 # 线圈半径 cm
    d = R    # 亥姆霍兹条件：线圈间距 = 半径
    # 公式：两个单线圈磁场的叠加
    term1 = 1 / (R**2 + (x - d/2)**2)**1.5
    term2 = 1 / (R**2 + (x + d/2)**2)**1.5
    return C * (term1 + term2)

# 使用最小二乘法拟合参数 C (包含电流、匝数等常数的系数)
popt, pcov = curve_fit(helmholtz_field, X_vals, B_measured)
C_optimal = popt[0]

# 生成平滑曲线数据用于绘图
X_smooth = np.linspace(min(X_vals), max(X_vals), 300)
B_smooth = helmholtz_field(X_smooth, C_optimal)

# 绘图
plt.figure(figsize=(10, 6))
plt.scatter(X_vals, B_measured, color='red', label='测量值 (mT)', zorder=5)
plt.plot(X_smooth, B_smooth, color='blue', label='理论值', linewidth=2)

plt.title('亥姆霍兹线圈轴线上磁场分布', fontsize=14)
plt.xlabel('距中心距离(cm)', fontsize=12)
plt.ylabel('磁感应强度 B (mT)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.axvline(x=0, color='gray', linestyle=':', alpha=0.5) # 标记中心

plt.savefig('helmholtz_fit.png')