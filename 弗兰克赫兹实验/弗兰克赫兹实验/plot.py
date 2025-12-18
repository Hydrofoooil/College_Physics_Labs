import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False                 # 解决负号 '-' 显示为方块的问题

# 1. 准备数据
u_data = np.arange(0.5, 100.5, 0.5)
i_data = np.array([
    0, 0, 0, 0, 3, 31, 53, 94, 97, 121,
    152, 178, 210, 235, 242, 254, 268, 282, 297, 298,
    312, 321, 330, 336, 345, 352, 359, 364, 371, 378,
    383, 389, 394, 398, 401, 402, 401, 393, 383, 368,
    351, 342, 346, 360, 380, 404, 418, 436, 453, 467,
    479, 491, 501, 511, 518, 522, 522, 518, 508, 494,
    472, 446, 428, 425, 437, 456, 480, 503, 525, 545,
    562, 578, 592, 606, 615, 623, 629, 631, 631, 627,
    618, 606, 585, 550, 533, 520, 525, 543, 566, 591,
    615, 640, 669, 676, 694, 705, 717, 724, 730, 733,
    734, 733, 728, 721, 706, 690, 665, 641, 627, 628,
    645, 662, 686, 712, 731, 754, 773, 789, 802, 815,
    825, 833, 838, 841, 841, 839, 835, 826, 811, 789,
    774, 757, 748, 750, 762, 777, 798, 819, 842, 860,
    879, 897, 914, 927, 939, 949, 958, 962, 965, 965,
    962, 955, 944, 931, 918, 903, 887, 896, 899, 910,
    925, 941, 961, 977, 997, 1018, 1035, 1052, 1067, 1081,
    1095, 1105, 1111, 1116, 1118, 1116, 1112, 1105, 1096, 1085,
    1081, 1077, 1078, 1081, 1090, 1100, 1114, 1130, 1147, 1168,
    1183, 1202, 1224, 1240, 1257, 1272, 1283, 1296, 1306, 1317
])

# 2. 插值拟合
# 生成更密集的 x 坐标，使曲线圆滑
u_smooth = np.linspace(u_data.min(), u_data.max(), 500)
# k=3 代表三次样条插值
spl = make_interp_spline(u_data, i_data, k=3)
i_smooth = spl(u_smooth)

# 3. 绘图
plt.figure(figsize=(12, 6))
# 画散点
plt.scatter(u_data, i_data, s=10, color='red', label='原始数据点', alpha=0.6)
# 画曲线
plt.plot(u_smooth, i_smooth, color='blue', linewidth=2, label='样条拟合曲线')

plt.title('弗兰克-赫兹实验 $I_A - U_{G2K}$ 拟合曲线', fontsize=15)
plt.xlabel('加速电压 $U_{G2K}$ (V)', fontsize=12)
plt.ylabel('板极电流 $I_A$ (nA)', fontsize=12)
plt.legend(prop={"family": "WenQuanYi Micro Hei", "size": 12})
plt.grid(True, linestyle='--', alpha=0.5)

# 保存
plt.savefig('franck_hertz_curve.png', dpi=300)
plt.show()