import numpy as np
import matplotlib.pyplot as plt

# --- Ubuntu 中文配置 ---
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False                 # 解决负号 '-' 显示为方块的问题

## 1. 准备数据
# X轴：电容值 C (uF)，注意原始数据的顺序是乱的，需要对应
x_data = np.array([0, 9, 8, 7, 6, 5, 4, 3, 2, 1])
# Y轴：功率因数 lambda (用户提供的新数据)
y_data = np.array([0.346, 0.379, 0.444, 0.602, 0.735, 0.874, 0.785, 0.652, 0.494, 0.468])

# 2. 数据排序 (绘图需要 X 从小到大排列)
sorted_indices = np.argsort(x_data)
x_sorted = x_data[sorted_indices]
y_sorted = y_data[sorted_indices]

# 3. 曲线拟合
# 使用 5次多项式拟合 (degree=5) 来平滑连接这些点
# polyfit 返回多项式系数，poly1d 生成多项式函数对象
z = np.polyfit(x_sorted, y_sorted, 5)
p = np.poly1d(z)

# 生成平滑曲线用的点 (从 0 到 9 生成 300 个点)
x_smooth = np.linspace(x_sorted.min(), x_sorted.max(), 300)
y_smooth = p(x_smooth)

# 4. 绘图
plt.figure(figsize=(10, 6)) # 设置画布大小

# 画散点 (原始数据)
plt.scatter(x_sorted, y_sorted, color='red', marker='o', s=50, label='实验数据点', zorder=5)

# 画拟合曲线
plt.plot(x_smooth, y_smooth, color='blue', linewidth=2, label='多项式拟合曲线')

# 添加标签和标题
plt.title('功率因数 $\lambda$ 与电容 $C$ 关系曲线', fontsize=15) # 需确保环境支持中文，否则用英文
plt.xlabel('电容 $C$ ($\mu$F)', fontsize=12)
plt.ylabel('功率因数 $\lambda$', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6) #哪怕网格线
plt.legend()

# 显示图片
plt.show()