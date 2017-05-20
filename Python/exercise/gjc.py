# -*- coding: utf-8 -*-
"""
Created on Wed May  3 11:40:37 2017

@author: Isola
"""

import pandas as pd
import numpy as np
#import jieba
import matplotlib.pyplot as plt
#import seaborn as sns

#from wordcloud import WordCloud , STOPWORDS#, ImageColorGenerator
#import os 
from os import  chdir


# 读取数据
chdir('E:\\coding\\Spyder\\exercise')
time11 = pd.read_csv( '.\\gjc\\time11.csv', header = 0,encoding = 'utf-8')
time12 = pd.read_csv( '.\\gjc\\time12.csv', header = 0,encoding = 'utf-8')
time13 = pd.read_csv( '.\\gjc\\time13.csv', header = 0,encoding = 'utf-8')
time09 = pd.read_csv( '.\\gjc\\time09.csv', header = 0,encoding = 'utf-8')
time10 = pd.read_csv( '.\\gjc\\time10.csv', header = 0,encoding = 'utf-8')


                  

plt.plot(time11['date'],time11['num'],color="red") #折线图
plt.plot(time12['date'],time12['num'],color = 'g') #折线图
plt.plot(time13['date'],time13['num'],color = 'b') #折线图
plt.plot(time09['date'],time09['num'],color = 'c') #折线图
plt.plot(time10['date'],time10['num'],color = 'y',label=file_name) #折线图
plt.xlabel("date")
plt.ylabel("num")
plt.title(" Example")
plt.legend()
plt.show()



                  
## 导入库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from os import  chdir

# 读取数据
chdir('E:\\coding\\Spyder\\exercise')
## 构建数据
data = pd.read_csv( '.\\gjc\\gjc.csv', header = 0,encoding = 'utf-8')
data = data.dropna() #去除缺失
data_gps = data[['经度','纬度']]
plt.scatter(data[['经度']],data[['纬度']]) #散点图

#DBSCAN 密度聚类
#data_gps = StandardScaler().fit_transform(data_gps)
db = DBSCAN(eps=0.005, min_samples=3).fit(data_gps)  #,metric='euclidean'
#print('聚类标签为：',db.labels_)
data_gps['clas'] = db.labels_
data['clas'] = db.labels_
#删除噪声行 
data_gps = data_gps[data_gps['clas'] > 0]
data_gps = data_gps.reset_index()
data_gps.shape
#data_gps['clas'].value_counts()     
plt.scatter(data_gps['经度'],data_gps[['纬度']],c = data_gps['clas']) #散点图

            
 
#上车人数
dcount =  data_gps['clas'].value_counts()   
#dcount = dcount.sort_index()   
dcount = pd.DataFrame(dcount.sort_index())        
#下车人数
#D =    


#概率矩阵计算
#权重
dcount['wj'] =  dcount.values / dcount.values.sum() 

#概率
import math
def fc(i,j): #从i站到j站
    if i > j or i == j:
        return 0
    else:
        v,y = 0,0
        for x in range(i+1,j+1):
            y += x
        v = y/(j-i)
        return  pow(np.e,(-v)) * pow(v,(j-i)) / math.factorial(j-i)


#泊松分布
   
lmd = 0    
for i in range(1,dcount.shape[0]+1):
    lmd +=i
lmd = lmd/dcount.shape[0]

pro = pd.DataFrame(np.zeros((dcount.shape[0],dcount.shape[0]+1)))

for i in range(dcount.shape[0]):
    for j in range(dcount.shape[0]):
        if (i < j):
            f = ((math.e)**(-lmd) * lmd**(j-i)) / math.factorial(j-i)
            pro.iloc[i,j] = f
    pro.iloc[i,dcount.shape[0]] = sum(pro.iloc[i,:dcount.shape[0]] * dcount['wj'])    
    
# 构建OD矩阵,求出一个站点到另一个站点的下车人数
# 此处的X是车站点总数 
# 创建数据框
df_OD = pd.DataFrame(np.zeros((k+1,k+1)))
for i in range(k):
    for j in range(k):
        if (i < j):
            p = pro.iloc[i,j]*df_wj.iloc[j] / pro.iloc[i,k]
            df_OD.iloc[i,j] = round(p * df_result.iloc[i,1])




