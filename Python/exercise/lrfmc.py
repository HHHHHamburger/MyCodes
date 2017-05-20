# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:13:09 2017

@author: Isola
"""

from pylab import *
#import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import datetime
from sklearn import preprocessing
from sklearn.cluster import KMeans
#import matplotlib.pyplot as plt

#读取问题 对excel的操作  强制utf-8
airline_data = pd.read_csv("../air_data.csv",header = 0) #,encoding = 'gbk'
#arda = pd.read_table("../air_data.csv",sep = ',',header = None,encoding = 'big5')
#arda = csv.reader(open("../air_data.csv"))
airline_data.head()
#数据探索： 1、数据记录的详细程度； 2、理解每个变量的含义； 3、数据质量分析； 4、理解数据和所要研究的项目目标之间的关系；
airline_data.shape  #查看维度
explore_data = airline_data.describe().T

explore_data["null"] = len(airline_data) - explore_data["count"]
airline_notnull = airline_data[airline_data["SUM_YR_1"].notnull()&airline_data["SUM_YR_2"].notnull()]
#index1 = airline_notnull["SUM_YR_1"] == 0
#index2 = airline_notnull["SUM_YR_2"] == 0
#index3 = (airline_notnull["SEG_KM_SUM"] != 0) & (airline_notnull["avg_discount"] > 0)
#airline_explore = airline_notnull[index1|index2|index3]  #找出第一年里程为0 或者第二年里程为零 或者总里程不为0折扣大于0
airline_explore = airline_notnull
airline_selection = airline_explore[["FFP_DATE","LOAD_TIME","FLIGHT_COUNT","LAST_TO_END","avg_discount","SEG_KM_SUM"]]
L = pd.to_datetime(airline_selection["LOAD_TIME"]) - pd.to_datetime(airline_selection["FFP_DATE"])
L = L.astype("str").str.split().str[0]
L = L.astype("int")/30
#客户最近一次乘坐公司飞机距观测窗口结束的月数
R = airline_selection["LAST_TO_END"]
#客户在观测窗口内乘坐公司飞机的次数 = 观测窗口的飞行次数[单位：次]
F = airline_selection["FLIGHT_COUNT"]
#客户在观测时间内在公司累计的飞行里程 = 观测窗口总飞行公里数[单位：公里]
M = airline_selection["SEG_KM_SUM"]
#客户在观测时间内乘坐舱位所对应的折扣系数的平均值 = 平均折扣率[单位：无]
C = airline_selection["avg_discount"]
airline_features = pd.concat([L,R,F,M,C],axis = 1)
airline_features.columns = ["L","R","F","M","C"]

airline_scale = (airline_features - airline_features.mean(axis =0))/airline_features.std(axis=0)
#airline_Minmaxscale = (airline_features.min())/(airline_features.max()-airline_features.min())
plt.plot(airline_features)
plt.plot(airline_scale)
kmeans_model = KMeans(n_clusters = 5,n_jobs=4)

fit_kmeans = kmeans_model.fit(airline_scale)
r1 = pd.Series(kmeans_model.labels_).value_counts() #统计不同类别样本的数目
r2 = pd.DataFrame(kmeans_model.cluster_centers_) #将聚类中心转化为数据框
r = pd.concat([r1,r2],axis=1)
r.columns = ["类别数目"] + list(airline_scale.columns) #表格重命名


#——————————————————————————————————————————————————————————————————————————————————
#dataframe 的操作 读取某行某列
df = pd.DataFrame(airline_data, columns=['FFP_DATE','LOAD_TIME','FLIGHT_COUNT','SEG_KM_SUM', 'LAST_TO_END','avg_discount'])
ffdDate = df['FFP_DATE'].apply(lambda x:datetime.strptime(x,'%Y/%m/%d') )
loadDate =  df['LOAD_TIME'].apply(lambda x:datetime.strptime(x,'%Y/%m/%d') )
#datetime.strptime('2012/12/21','%Y/%m/%d')
#a = datetime(2012, 9, 23)
#b = datetime(2012, 12, 21)
#d = relativedelta(ffdDate[0], loadDate[0])
ffdMonths=['']
for i in ffdDate.index:
    rel = relativedelta(loadDate[i],ffdDate[i])
    if rel.days > 0:
        ffdMonths.append(rel.months+rel.years*12+1)
    else:
        ffdMonths.append(rel.months+rel.years*12)
ffdMonths.remove(ffdMonths[0])
Resdf = pd.concat([df, pd.DataFrame(ffdMonths,columns=['FFD_MONTHS'])], axis=1)   #索引合并 标签拼接
del Resdf['FFP_DATE']
del Resdf['LOAD_TIME']

Resdf_minmax = preprocessing.MinMaxScaler().fit_transform(Resdf) #数据标准化
plt.plot(Resdf_minmax)
#k-means
model = KMeans(n_clusters=5)
ResdfKmeans = model.fit(Resdf_minmax)
#print(ResdfKmeans)
#print('聚类中心为:', ResdfKmeans.cluster_centers_)
#print('类别标签为', ResdfKmeans.labels_)
#print('样本到最近聚类中心距离之和为', ResdfKmeans.inertia_)

Resdfcls = pd.concat([Resdf, pd.DataFrame(ResdfKmeans.labels_,columns=['flag'])], axis=1)   #索引合并 标签拼接

                     
                     
                     
                 
# 散点图
plt.figure(figsize =(8,4))
#plt.subplot(221)
plt.scatter(Resdfcls[Resdfcls.flag==0]['FFD_MONTHS'], Resdfcls[Resdfcls.flag==0]['FLIGHT_COUNT'], color='g')
plt.scatter(Resdfcls[Resdfcls.flag==1]['FFD_MONTHS'], Resdfcls[Resdfcls.flag==1]['FLIGHT_COUNT'], color='c')
plt.scatter(Resdfcls[Resdfcls.flag==2]['FFD_MONTHS'], Resdfcls[Resdfcls.flag==2]['FLIGHT_COUNT'], color='r')
plt.scatter(Resdfcls[Resdfcls.flag==3]['FFD_MONTHS'], Resdfcls[Resdfcls.flag==3]['FLIGHT_COUNT'], color='b')
plt.scatter(Resdfcls[Resdfcls.flag==4]['FFD_MONTHS'], Resdfcls[Resdfcls.flag==4]['FLIGHT_COUNT'], color='y')



