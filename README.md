# Hydrofoil 的大雾实验报告

## 关于这个仓库

该仓库中含有：

- 本人所选实验的实验报告 LaTeX 全文源码，以及相应配图、字体文件等，克隆至本地即可编译
- 预习报告和实验报告各自分装，位于同一实验文件夹下
- 需要拟合曲线的实验报告，在文件夹中附带了 Python 拟合绘图脚本，在 py 文件里替换自己的数据后直接运行脚本即可
- 附带大雾实验教材 PDF 版，供大家摘抄，或按需截取配图插入自己的实验报告
- 保留了我的实验原始数据（去掉了助教签名），供不太会做实验的同学边做边借鉴（懂得都懂）

该仓库每周持续更新直至课程结束，文件夹名末尾的数字为“得分（总分）”，例如“85（90）”即为满分 90 分（因为必做实验不包含预习报告），得分 85。没标出即为未出分

## Quick Start

### 环境配置

1. **安装 LaTeX 编译器**
   - macOS: `brew install --cask mactex` 或使用 MacTeX
   - Linux: `sudo apt-get install texlive-full` (Ubuntu/Debian) 或 `sudo yum install texlive-scheme-full` (CentOS/RHEL)
   - Windows: 下载并安装 [TeX Live](https://www.tug.org/texlive/)

2. **安装中文字体（SimSun）**

   项目使用 SimSun（宋体）字体进行中文排版。请根据你的操作系统安装字体：

   - **macOS**:

     ```bash
     # 将 SimSun.ttf 复制到系统字体目录
     cp SimSun.ttf ~/Library/Fonts/
     # 或者双击 SimSun.ttf 文件，点击"安装字体"
     ```

   - **Linux**:

     ```bash
     # 复制到用户字体目录
     mkdir -p ~/.fonts
     cp SimSun.ttf ~/.fonts/
     fc-cache -fv  # 刷新字体缓存
     ```

   - **Windows**:
     - 双击 `SimSun.ttf` 文件，点击"安装"按钮
     - 或复制到 `C:\Windows\Fonts\` 目录

3. **安装 Python 依赖**

   ```bash
   pip install -r requirements.txt
   ```

   或使用虚拟环境：

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # 或 venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

### 使用步骤

1. 克隆仓库到本地

   ```bash
   git clone <repository-url>
   cd College_Physics_Labs
   ```

2. 安装中文字体（SimSun）

   项目根目录下的 `SimSun.ttf` 需要安装到系统中，请参考上方"环境配置"部分的字体安装说明。

3. 安装 Python 依赖（如需运行绘图脚本）

   ```bash
   pip install -r requirements.txt
   ```

4. 使用 VSCode 打开项目（建议安装 `LaTeX Workshop` 插件）

5. **编译实验报告**

   项目提供了 Makefile，可以一键编译所有实验报告：

   ```bash
   # 编译所有实验报告
   make

   # 查看所有需要编译的文件
   make list

   # 编译单个文件
   make compile TEX=光栅衍射实验/光栅衍射实验/实验报告.tex

   # 清理编译中间文件
   make clean

   # 清理所有 PDF 文件
   make clean-pdf

   # 查看帮助
   make help
   ```

   或者使用 VSCode 的 LaTeX Workshop 插件手动编译单个文件。

6. 如需运行 Python 绘图脚本：
   - 进入对应实验文件夹
   - 编辑 `plot.py` 文件，替换为你自己的数据
   - 运行 `python plot.py` 生成图表

## 目录

| 实验名称 | 实验报告 | 预习报告 | 分数 |
|---------|---------|---------|------|
| 光栅衍射实验 | [实验报告](光栅衍射实验/光栅衍射实验/实验报告.tex) | [预习报告](光栅衍射实验/光栅衍射实验预习/实验报告.tex) | 未出分 |
| 分光计的调整和使用 | [实验报告](分光计的调整和使用85(90)/实验报告.tex) | - | 85/90 |
| 双臂电桥测低电阻 | [实验报告](双臂电桥测低电阻87(100)/双臂电桥/实验报告.tex) | [预习报告](双臂电桥测低电阻87(100)/双臂电桥预习/实验报告.tex) | 87/100 |
| 惠斯登电桥 | [实验报告](惠斯登电桥90(100)/惠斯登电桥/实验报告.tex) | [预习报告](惠斯登电桥90(100)/惠斯登电桥预习/实验报告.tex) | 90/100 |
| 棱镜偏向角特性 | [实验报告](棱镜偏向角特性86(100)/棱镜偏向角特性/实验报告.tex) | [预习报告](棱镜偏向角特性86(100)/棱镜偏向角特性预习/实验报告.tex) | 86/100 |
| 示波器的使用 | [实验报告](示波器的使用85(90)/实验报告.tex) | - | 85/90 |
| 非平衡电桥 | [实验报告](非平衡电桥95(100)/非平衡电桥/实验报告.tex) | [预习报告](非平衡电桥95(100)/非平衡电桥预习/实验报告.tex) | 95/100 |

<!-- TODO: 补充剩余实验/填写对应分数 -->

## 友情链接

@FLOG 司马：[【大学物理实验/大物实验/普通物理学实验/普物实验】实验报告整合 - CC98 论坛](https://www.cc98.org/topic/6340287)

@菜白：[【大学物理实验/大物实验】2023-2024秋冬学期回忆卷+资源汇总整理分享 - CC98 论坛](https://www.cc98.org/topic/5802063)

@马二马纯上：[大学物理实验/大物实验 资源索引 - CC98 论坛](https://www.cc98.org/topic/5862194)

@Mchromo：[自己做的大物实验绪论ppt - CC98论坛](https://www.cc98.org/topic/5078578)

@c98c98898：[求助大物实验历年卷答案](https://www.cc98.org/topic/6085479)

@FLOG司马：[【实验报告】大学物理实验/大物实验/普物实验 参考实验报告 23-24秋冬真题卷/历年卷](https://www.cc98.org/topic/5845216)

## 后记

**大雾实验作为浪费大量时间又从各个层面都毫无用处的毫无疑问的依托**，是理工科同学必须跨过的一道磨难，本学期实验报告改为了电子版，相对于历年的手抄实验报告应有缓解。然而对于追求报告质量的同学，每周仍需花费 4 小时以上时间（以 lz 为例）使用 LaTeX 排版来形成一份精美的报告，真是传统教育的余孽。为了之后的同学就此摆脱这被赋予我们的桎梏，lz 敬上自己排版的 LaTeX 实验报告，以后大家就 **只需要替换一下自己的数据/思考题即可获得自己的极高质量报告，每周工作量不超过半小时。** 希望大家的学业负担能够少一些，有更多时间用于玩和自我提升！

## License

<!-- TODO: 添加 license -->

## Contributing

欢迎大家提交 pull request，一起完善这个仓库，让之后的同学能够更加轻松地完成实验报告。

![star history](https://api.star-history.com/svg?repos=Hydrofoooil/College_Physics_Labs&type=Date)

![contributors](https://contrib.rocks/image?repo=Hydrofoooil/College_Physics_Labs)

