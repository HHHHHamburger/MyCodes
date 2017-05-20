# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 15:00:15 2017

@author: Isola
"""

from pylab import *
import pandas as pd
#import numpy as np
from scipy.interpolate import lagrange #导入拉格朗日插值函数


#plt.plot() 折线图
#plt.hist() 直方图
#plt.bar() 柱状图
#plt.scatter() 散点图
#plt.pie() 饼图
#plt.boxplot() 箱线图


StealUserdiStribute = pd.read_csv('E:\coding\Data\CSG\\01-explorer Steal user distribute.csv',encoding = 'GBK')
StealUser = pd.read_csv('E:\coding\Data\CSG\\01-explorer Steal user.csv',encoding = 'GBK')
user = pd.read_csv('E:\coding\Data\CSG\\01-explorer user.csv',encoding = 'GBK')
preprocessed = pd.read_csv('E:\coding\Data\CSG\\02-preprocessed missing_data.csv',encoding = 'GBK',names = ['a','b','c'])
lineLoss = pd.read_csv('E:\coding\Data\CSG\\04-line loss line_loss.csv',encoding = 'GBK')
electricityDescend = pd.read_csv('E:\coding\Data\CSG\\03- electricity quantity to descend electricity.csv',encoding = 'GBK')



#统计出各个类的个数
Industry = StealUserdiStribute.groupby('Industry').count()
StealUserdiStribute['Industry']
shape = Industry.shape

plt.figure(22,figsize=(15,9))
plt.subplot(211)
plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
#plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
plt.bar(range(shape[0]),Industry.sort(columns = 'User',ascending = False )['User'],width = 0.1)
plt.xticks(range(shape[0]),Industry.sort_values('User',ascending = False).index)
plt.title(u'用户类别窃漏电情况',size=15)
plt.ylabel(u'窃漏电用户数',size=15)

shape = user.shape

#画出正常用户的图形  
plt.subplot(223)
#plt.plot(pd.date_range('20120201',periods=shape[0]).tolist,user['Eletricity'],color="red",linewidth=2)
plt.plot_date( user['Date'],user['Eletricity'],'-',xdate=True)
plt.title(u'正常用户用电量趋势',size=15)
plt.ylabel(u'日用电量',size=15)
plt.legend(loc=1)
plt.xticks(rotation=40)#设置x标签的显示角度


#画出窃电用户的图形
#plt.plot(StealUser['Date'],pd.date_range('20120201',periods=shape[0]),label="$StealUser['Eletricity']$",color="red",linewidth=2)
plt.subplot(224)
plt.plot_date(StealUser['Date'],StealUser['Eletricity'],'-',xdate=True)
plt.title(u'窃电用户用电量趋势',size=15)
plt.ylabel(u'日用电量',size=15)
plt.xticks(rotation=40)
plt.legend(loc=1)
plt.show()

#对缺失值进行拉格朗日插值法补充
#①
for colm in preprocessed.columns:   
    a = preprocessed[colm].isnull()   
    index = a[a==True].index   
    for i in index:   
        x = a.index[(~a) & (np.abs(a.index-i)<= 5) & (a.index!=i)].values   
        w = preprocessed[colm].ix[x].values   
        preprocessed[colm].ix[i] = lagrange(x,w)(i)
#②
#自定义列向量插值函数
#s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def lagrange_elec(s, n, k=5): 
  y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] #计算缺失值前5天非空的个数(n是空值，n-k即前k个数），后5天（n+1空值，n+1+k)后五天非空个数
  y = y[y.notnull()]                                   #剔除空值，因为是根据已知的数据构造插值公式的近似未知的值
  return lagrange(y.index, list(y))(n)                 #插值并返回插值结果，y.index已知数据，list(y)(n) 需要插值的位置

for i in data.columns:                              #判断i是否在每一列中
  for j in range(len(data)):                        #判断j是否在每一行中
    if (data[i].isnull())[j]:                       #如果为空即插值。
      data[i][j] = lagrange_elec(data[i], j)
      
#构建特征三个向量
#电量趋势下降指标
ele = electricityDescend['electricity']
#plt.plot( electricityDescend['Line loss']) 
#np.cov(ele[:5])
#①
for i in range(5):
    np.cov(ele[:5])
np.cov
np.var

one = np.var(ele[:11])/np.cov(ele[:11])

d=[0]
for c in np.arange(11,38):
    k1,k2 = 0,0
    for i in np.arange(c-11,c):
        f = ele[c-11:c].sum()/11
        l = np.arange(c).sum()/11
        k1 += (ele[i]-f)*(i-l)
        k2 += (i-l)*(i-l)
    d.append(k1/k2) 

#②
k = [] 
for i in range(length):
    if i <= 4:
        l = range(0,(i+6))                          #i-5不满足5天，求斜率天数取值为l
        s = np.cov(down[0:(i+6)],l)[1,0]/np.var(l)  #协方差的输入为两个一维数组，返回值为协方差矩阵；分母为样本方差
    if 4 < i <= (length-6):#当天及后五天合计六天
        l = range((i-5),(i+6))                      #i-5及i+6均满足5天求斜率的天数取值为l
        s = np.cov(down[(i-5):(i+6)],l)[1,0]/np.var(l)  
    if i > (length-6):
        l = range((i-5),length)                      #i+5不满足5天，求斜率天数取值为l
        s = np.cov(down[(i-5):length],l)[1,0]/np.var(l)
    k.append(s)
des = []
for i in range(1,length): 
    if k[i] < k[i-1]:
        des.append(1)       
    else:
        des.append(0)
len(des) 
total = []
for i in range(length):
    if i < 4:
        m = sum(des[0:(i+6)])
    if 4 < i < (length-6):
        m = sum(des[(i-4):(i+6)]) #统计求和不计算第一天的数值，从第二天开始
    if i > (length-6):
        m = sum(des[(i-4):length])#统计求和不计算第一天的数值，从第二天开始
    total.append(m)
    

#③
eleData=pd.read_csv("./02-Data(new)/03- Power down/electricity.csv",encoding="gb18030")
eleData=eleData.drop("Line loss",axis=1)
eleData["Elec"]-np.mean(eleData["Elec"])
eleData["k"]=0.0
eleData["D"]=0
eleData["T"]=0
for i in eleData.index:
    l=eleData.index[np.abs(eleData.index-i)<=5].values
    f=eleData.ix[l,"Elec"].values
    res=sum((l-np.mean(l))*(f-np.mean(f)))/(len(l)*np.var(l))
    eleData.ix[i,"k"]=res
for i in range(1,len(eleData)):
    if eleData.ix[i,"k"] < eleData.ix[i-1,"k"]:
        eleData.ix[i,"D"]=1
for i in eleData.index:
    l=eleData.index[(np.abs(eleData.index-i)<=5)].values
    eleData.ix[i,"T"]=sum(eleData.ix[l[1:],"D"].values)
      
#线损指标
lineLoss = lineLoss['Line loss']
shape = lineLoss.shape
lineLoss['tl'] = (lineLoss['Output']-lineLoss['Input'])/lineLoss['Output']

loss = []
for c in np.arange(shape[0]):
    if c < 4:
        v1 = lineLoss['tl'][c:c+6].sum()/5
        v2 = lineLoss['tl'][:c+1].sum()/5
        if ((v1-v2)/v2) > 0.01:
            loss.append(1)
        else :
            loss.append(0)
    elif c < shape[0]-5:
        v1 = lineLoss['tl'][c:c+6].sum()/5
        v2 = lineLoss['tl'][c-5:c].sum()/5
        if ((v1-v2)/v2) > 0.01:
            loss.append(1)
        else :
            loss.append(0)
    else:
        v1 = lineLoss['tl'][c:shape[0]].sum()/5
        v2 = lineLoss['tl'][c-5:c].sum()/5
        if ((v1-v2)/v2) > 0.01:
            loss.append(1)
        else :
            loss.append(0)

#告警类指标
alarm = pd.read_csv('E:\coding\Data\CSG\\05-alarm 告警.csv',encoding = 'GBK')
usrAlarm = pd.read_csv('E:\coding\Data\CSG\\05-alarm 用户.csv',encoding = 'GBK')

x = pd.merge(alarm,usrAlarm,on=['ID','date'])  #丢失了数据

alarm_num = alarm.groupby(['ID','date']).count()
alarm_num.reset_index(inplace = True) #重新按行设置索引
alarm_final = pd.concat([usrAlarm,alarm_num],keys = ('ID','date'),join = "outer")  #合并表

index_null = alarm_final["alarm"].isnull()  #找到报警数据为空的位置
alarm_final.loc[index_null,"alarm"] = alarm_final.loc[index_null,"alarm"].fillna(0)  #把为空的位置填从为0


#构建模型
from sklearn.tree import DecisionTreeClassifier #导入决策树的库
from sklearn.metrics import accuracy_score   #准确度
from sklearn.metrics import average_precision_score
from sklearn.metrics import f1_score
from sklearn.cross_validation import train_test_split

tree_model = pd.read_csv('E:\coding\Data\CSG\\06-model model.csv',encoding = 'GBK')
testData = pd.read_csv('E:\coding\Data\CSG\\06-model testData.csv',encoding = 'GBK')
trainData = pd.read_csv('E:\coding\Data\CSG\\06-model trainData.csv',encoding = 'GBK')


#先把样本分成训练集 和测试集
X = tree_model.iloc[:,0:4]
y = tree_model.iloc[:,-1]

#LM神经网络
from keras.models import Sequential #导入神经网络初始化函数
from keras.layers.core import Dense, Activation #导入神经网络层函数、激活函数
net = Sequential() #建立神经网络
net.add(Dense(input_dim=3,output_dim=10)) #添加输入层（3节点）到隐藏层（10节点）的连接
#net.add(Dense(32, input_dim=16))
net.add(Activation('relu')) #隐藏层使用relu激活函数
net.add(Dense(input_dim=10, output_dim=1)) #添加隐藏层（10节点）到输出层（1节点）的连接
net.add(Activation('sigmoid')) #输出层使用sigmoid激活函数
net.compile(loss = 'binary_crossentropy', optimizer = 'adam', class_mode = "binary") #编译模型，使用adam方法求解

net.fit(train[:,:3], train[:,3], nb_epoch=2, batch_size=1) #训练模型，循环1000次,Keras模块中的batch_size指的就是小批量梯度下降法。
net.save_weights(netfile) #保存模型

from sklearn.metrics import roc_auc_score
roc_auc_score(y_test,proba)                 #查看AUC的值，注意的地方AUC的参数是预测的概率值


X_train, X_test, y_train, y_test= train_test_split(X,y,test_size = 0.2,random_state =1)
clf.fit(X_train.iloc[:,1:],y_train) #模型训练
y_pred = clf.predict(X_test.iloc[:,1:])   #预测新样本
proba = clf.predict_proba(X_test.iloc[:,1:])[:,1] #预测概率值   没做
pd.Series(y_pred).value_counts() #统计预测结果类别
accuracy_score(y_test,y_pred)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
from sklearn.metrics import recall_score  #查全率75%即所有的窃电用户有75%的比例被查出来 【漏判】
recall_score(y_test, y_pred)
from sklearn.metrics import precision_score  #查出来的用户有66%用户为窃电用户 【误判】
precision_score(y_test,y_pred)
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))
from sklearn.metrics import roc_auc_score
roc_auc_score(y_test,proba)                 #查看AUC的值，注意的地方AUC的参数是预测的概率值
from sklearn.metrics import roc_curve
fpr,tpr,thresholds = roc_curve(y_test,proba,pos_label=1) #构建ROC曲线图，pos_label=1表示正类的类别标记 = 1
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
plt.plot(fpr,tpr,linewidth = 2,label ="ROC of CART")
plt.xlabel("False positive Rate")
plt.ylabel("True positive Rate")
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc =4) #图例及位置

          
          
#把测试集样本整理好 这里有四个维度
trainData.columns
x = trainData[['ele_ind','loss_ind','alarm_ind']]
y = trainData['class']

#fit
clf = DecisionTreeClassifier().fit(x, y)

#测试
x2 = testData[['ele_ind','loss_ind','alarm_ind']]
y2 = testData['class']
p = clf.predict(x2)

#评价   不够
m1 = accuracy_score(y2,p) 
m2 = average_precision_score(y2,p)
m3 = f1_score(y2,p)
#roc 曲线
#auc 曲线

import os
import pandas as pd
import matplotlib.pyplot as plt
#设置工作目录
os.chdir(r"F:\大数据学习\案例\02-电力窃漏电用户自动识别")
#获取不同行业窃电数据
filepath=U"01-explorer\\Steal user distribute.csv"
data_explorer = pd.read_csv(filepath,encoding="gb18030")
#获取正常用户用电数据
user = pd.read_csv(r"01-explorer\user.csv")
#获取非正常用户用电数据
steal_user = pd.read_csv("01-explorer\Steal user.csv")
#获取所有漏电行业分类
data_classify = data_explorer[['Industry']]
#统计漏电
data_s = data_classify['Industry'].value_counts()
x = list(data_s.index)
y = list(data_s)
#正常用户用电趋势
x1 = user['Date']
y1 = user['Eletricity']
#非正常用户用电趋势
x2 = steal_user['Date']
y2 = steal_user['Eletricity']
#解决编码问题
plt.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
#plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
#画图
#用户类别窃漏电情况
plt.figure(22,figsize=(15,9))
plt.subplot(211)
plt.bar(range(len(y)),y,width=0.5,linewidth=0)
plt.title(u'用户类别窃漏电情况',size=15)
plt.ylabel(u'窃漏电用户数',size=15)
plt.xticks(range(len(y)),x)
#正常用户用电量趋势
plt.subplot(223)
#plt.plot_date(x1,y1,linestyle='--',xdate=True)
plt.plot_date(x1,y1,'-',xdate=True)
plt.title(u'正常用户用电量趋势',size=15)
plt.ylabel(u'日用电量',size=15)
plt.legend(loc=1)
#设置x标签的显示角度
plt.xticks(rotation=40)
#窃电用户用电量趋势
plt.subplot(224)
plt.plot_date(x2,y2,'-',xdate=True)
plt.title(u'窃电用户用电量趋势',size=15)
plt.ylabel(u'日用电量',size=15)
plt.xticks(rotation=40)
plt.legend(loc=1)
plt.show()

