# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 17:04:33 2017

@author: Isola
"""

# 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
from pylab import *

# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
figure(figsize=(8,6), dpi=80)

# 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
subplot(1,1,1)

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

# 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
plot(X, S, color="green", linewidth=1.0, linestyle="-")

# 设置横轴的上下限
xlim(-4.0,4.0)

# 设置横轴记号
xticks(np.linspace(-4,4,9,endpoint=True))

# 设置纵轴的上下限
ylim(-1.0,1.0)

# 设置纵轴记号
yticks(np.linspace(-1,1,5,endpoint=True))

# 以分辨率 72 来保存图片
# savefig("exercice_2.png",dpi=72)

# 在屏幕上显示
show()


plt.figure(figsize=(8,4))
plt.subplot(211)
data = [1, 0.5, -0.5,-1,-0.75,0.25,1,0.75,-0.25,-1]
plt.bar(range(len(data)), data,color='g')
plt.subplot(223)
data = np.random.randint(1, 11, 9)
plt.pie(data)
plt.subplot(224)
data = np.random.randint(1, 11, 5)
plt.boxplot(np.linspace(0,9,2))