import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pathlib import Path

# --- Ubuntu 中文配置 ---
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False                 # 解决负号 '-' 显示为方块的问题

# 1. 准备数据
# ==========================================================
# 示例数据：你可以替换为你自己的 x 和 y 列表
x_data = np.array([404.7 , 435.8 , 546.0, 577.1])
# 假设 y_data 接近某个非线性关系，并加入一些随机噪声（示例数据）
y_data = np.array([1.6846, 1.6734, 1.6544, 1.6520])

# 2. 选择非线性模型并拟合
# ==========================================================
# 可选模型：'quadratic' 二次多项式；'exponential' 指数；'power' 幂函数
MODEL = 'quadratic'  # 修改为 'exponential' 或 'power' 可切换模型

# 定义候选模型

def f_quadratic(x, a, b, c):
    return a * x**2 + b * x + c


def f_exponential(x, a, b, c):
    # a * exp(b x) + c
    return a * np.exp(b * x) + c


def f_power(x, a, b):
    # a * x^b（x 需为正）
    return a * np.power(x, b)

# 选择模型和初值
if MODEL == 'quadratic':
    func = f_quadratic
    p0 = [0.0, (y_data[-1] - y_data[0]) / (x_data[-1] - x_data[0]), y_data[0]]  # [a, b, c] 初猜
    param_names = ['a', 'b', 'c']
elif MODEL == 'exponential':
    func = f_exponential
    # 粗略初值：a≈幅度，b≈小斜率，c≈最小值
    a0 = (y_data.max() - y_data.min()) or 1.0
    b0 = 1e-2
    c0 = y_data.min()
    p0 = [a0, b0, c0]
    param_names = ['a', 'b', 'c']
elif MODEL == 'power':
    func = f_power
    # 幂函数需要 x>0，给出温和初值
    p0 = [1.0, 1.0]  # a, b
    param_names = ['a', 'b']
else:
    raise ValueError("未知模型，请将 MODEL 设为 'quadratic' | 'exponential' | 'power'")

# 执行非线性拟合
popt, pcov = curve_fit(func, x_data, y_data, p0=p0, maxfev=100000)
perr = np.sqrt(np.diag(pcov))  # 参数标准差（1-sigma 近似）

# 拟合评估：R^2
y_fit = func(x_data, *popt)
ss_res = np.sum((y_data - y_fit)**2)
ss_tot = np.sum((y_data - np.mean(y_data))**2)
r2 = 1 - ss_res / ss_tot if ss_tot != 0 else np.nan

# 3. 结果输出
# ==========================================================
print("非线性拟合结果 (MODEL = {}):".format(MODEL))
for name, val, err in zip(param_names, popt, perr):
    print(f"  {name} = {val:.6e} ± {err:.2e}")
print(f"  R^2 = {r2:.6f}")

# 4. 绘图
# ==========================================================
plt.figure(figsize=(10, 6))

# 原始数据：折线 + 散点
plt.plot(x_data, y_data,
         label='实验数据点',
         color='blue',
         linestyle='--',
         marker='o',
         alpha=0.6)
plt.scatter(x_data, y_data, color='blue', marker='o')

# 平滑曲线
x_smooth = np.linspace(np.min(x_data), np.max(x_data), 400)
y_smooth = func(x_smooth, *popt)

# 拟合曲线标签（展示前两个参数，避免过长）
if len(popt) == 3:
    label_fit = f"非线性拟合({MODEL}): a={popt[0]:.2e}, b={popt[1]:.2e}, c={popt[2]:.2e}"
else:
    label_fit = f"非线性拟合({MODEL}): a={popt[0]:.2e}, b={popt[1]:.2e}"

plt.plot(x_smooth, y_smooth,
         label=label_fit,
         color='red',
         linestyle='-',
         linewidth=2)

# 轴标签/网格/图例
plt.xlabel(r'波长$ \lambda $/nm', fontsize=14)
plt.ylabel(r'折射率n', fontsize=14)
plt.legend(loc='best')
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()

# 保存到脚本所在文件夹
out_path = Path(__file__).resolve().parent / 'nonlinear_fit_chart.jpg'
plt.savefig(out_path, dpi=300, quality=90, optimize=True)
print(f"图像已保存: {out_path}")

plt.show()