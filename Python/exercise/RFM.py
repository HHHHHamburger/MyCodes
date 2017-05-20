# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:25:24 2017

@author: Isola
"""
import pandas as pd
from sklearn.cluster import KMeans
from pylab import *

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']},
                     index=[0, 1, 2, 3])

df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
                  'D': ['D2', 'D3', 'D6', 'D7'],
                  'F': ['F2', 'F3', 'F6', 'F7']},
                 index=[2, 3, 6, 7])

table = pd.read_excel("..//RFM.xls")
sd = pd.DataFrame(table, columns=['R', 'F', 'M'])

model = KMeans(n_clusters=3,max_iter=500)

irisKmeans = model.fit(sd)

ad = pd.DataFrame(irisKmeans.labels_,columns=['clas'])
res =pd.DataFrame.join(sd,ad)
#res = sd.append(ad)
#res = pd.merge(sd,ad,left_index=True,right_index=True,how='outer') 
res1 = pd.concat([sd,ad],axis=1)   #  
res0 = pd.concat([sd,ad],axis=0)   # 
result1 = pd.concat([df1, df4], axis=1)   #索引合并 标签拼接
result0 = pd.concat([df1, df4], axis=0)   #索引拼接  标签合并 

sd['R']

figure(figsize=(8,6), dpi=80)
subplot(221)
scatter(sd['R'],sd['F'],)
subplot(222)

subplot(223)


from sklearn.cluster import KMeans
import sklearn.preprocessing
import pandas as pd
import os
# 设置工作路径
os.chdir('D:/TIPDM/课程培训/26 - PPV大数据机器学习2期/day-03/data')
# 读数据
df_dat = pd.read_excel('RFM.xls') 
rfm_data = df_dat.loc[:,['R','F','M']]
# 标准化
rfm_scaled = sklearn.preprocessing.scale(rfm_data)
# 建模
model = KMeans(n_clusters = 3)
irisKmeans = model.fit(rfm_scaled)
# 得到类标记
flag = pd.Series(irisKmeans.labels_, name=('flag'))
# 合并
df_result = pd.concat([df_dat,flag], axis=1)
# 输出
df_result.to_excel('RFM_result.xls')
# 散点图
import matplotlib.pyplot as plt
plt.figure(figsize =(8,4))
plt.subplot(221)
plt.scatter(df_result[flag==0]['R'], df_result[flag==0]['F'], color='m')
plt.scatter(df_result[flag==1]['R'], df_result[flag==1]['F'], color='c')
plt.scatter(df_result[flag==2]['R'], df_result[flag==2]['F'], color='r')
plt.subplot(222)
plt.scatter(df_result[flag==0]['R'], df_result[flag==0]['M'], color='m')
plt.scatter(df_result[flag==1]['R'], df_result[flag==1]['M'], color='c')
plt.scatter(df_result[flag==2]['R'], df_result[flag==2]['M'], color='r')
plt.subplot(223)
plt.scatter(df_result[flag==0]['F'], df_result[flag==0]['M'], color='m')
plt.scatter(df_result[flag==1]['F'], df_result[flag==1]['M'], color='c')
plt.scatter(df_result[flag==2]['F'], df_result[flag==2]['M'], color='r')


