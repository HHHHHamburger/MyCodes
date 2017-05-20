# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 02:55:39 2017

@author: Isola
"""

import numpy as np
import pandas as pd
x = np.arange(9).reshape(3,3)
y = np.arange(9).reshape(3,3)

np.linspace(0,30,10).shape
np.linspace(0,30,10).dnim
np.linspace(0,30,10).dtype

np.where(x>5)

a = np.vstack((x,y))
b = np.hstack((x,y))

c = np.vsplit(x,2)
d = np.hsplit(x,2)
e = np.identity(5) 
f = np.eye(5)

g = e == f


arr = np.array([[1,2,3],['a','b','c']])
df1 = pd.DataFrame(arr)


import numpy as np
import matplotlib.pyplot as plt
from pylab import *
x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()


## 导入库
import pandas as pd
import numpy as np
from sklearn.cross_validation import cross_val_score, ShuffleSplit
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor

#加载波士顿房价数据集，
boston = load_boston()
X = boston["data"]
Y = boston["target"]
names = boston["feature_names"]
##随机森林建模
rf = RandomForestRegressor(n_estimators=20, max_depth=4)
rfModel = rf.fit(X,Y)
##输出重要程度
impBoston= rfModel.feature_importances_ 
imp = pd.DataFrame(impBoston)
imp.columns = ['Importance']
imp.index = names
imp




for idx, color in enumerate("rgbyck"):
    plt.subplot(320+idx+1, axisbg=color)
plt.show()

plt.subplot(221) # 第一行的左图 
plt.subplot(222) # 第一行的右图 
plt.subplot(212) # 第二整行 
plt.show()


# 注释
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)
y = np.sin(x)

p1 = plt.plot(x, y, color = 'r')

plt.text(2,0.5,'mark')
plt.annotate('line', xy=(4.5,0.5), xytext=(3,0.6), arrowprops=dict(facecolor='blue', shrink=0.05),)

list(0.1,0.3,0.4,0.2)


import numpy as np
from scipy.integrate import odeint

from bokeh.plotting import figure, show, output_file

sigma = 10
rho = 28
beta = 8.0/3
theta = 3 * np.pi / 4

def lorenz(xyz, t):
    x, y, z = xyz
    x_dot = sigma * (y - x)
    y_dot = x * rho - x * z - y
    z_dot = x * y - beta* z
    return [x_dot, y_dot, z_dot]

initial = (-10, -7, 35)
t = np.arange(0, 100, 0.006)

solution = odeint(lorenz, initial, t)

x = solution[:, 0]
y = solution[:, 1]
z = solution[:, 2]
xprime = np.cos(theta) * x - np.sin(theta) * y

colors = ["#C6DBEF", "#9ECAE1", "#6BAED6", "#4292C6", "#2171B5", "#08519C", "#08306B",]

p = figure(title="lorenz example")

p.multi_line(np.array_split(xprime, 7), np.array_split(z, 7),
             line_color=colors, line_alpha=0.8, line_width=1.5)

output_file("lorenz.html", title="lorenz.py example")

show(p)  # open a browser


xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])


