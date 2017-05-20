# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 16:36:10 2017

@author: Isola
"""

'''
1.X1 LIMIT_BAL 代表额度
2.X2 GENDER 代表性别，1为男性，2为女性，值种类2种
3.X3 EDUCATION 代表受教育水平，值种类6种
4.X4 MARRIAGE 代表是否婚配，值种类4种
5.X4 AGE 代表年龄
6.X6-X11 PAY_0至PAY_6代表延期时间,从September-April；-1表示按时还款，-2表示未消费，正数代表延期几个月
7.X12-X17 BILL_AMT1至BILL_AMT6代表当期账单金额，从September-April
8.X18-X23 PAY_AMT1至PAY_AMT6代表当期还款金额，从September-April
9.Y是目标字段，代表是否违约
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 

os.chdir('E:\\coding\\Spyder\\exercise')
cardData = pd.read_excel('.\\data\\default of credit card clients.xlsx', header = 1,encoding = 'utf-8')
#data = data.dropna() #去除缺失

cardData.describe()
cardData.head()

#X6-X11 对违约的影响是相同的， 而且是同种类型，可以降维处理
#全部为-2 则转换为-1 全部为-1 转换成0   不管几个0 算1个1   有一次逾期就记一次

payData = cardData[['PAY_0','PAY_2','PAY_3','PAY_4','PAY_5','PAY_6']]

paydelay = []  #逾期时间
for card in payData.index:
    day0 = 0    #0 的个数
    day1 = 0    #-1 的个数
    day2 = 0    #-2 的个数
    day3 = 0    #大于0  的个数
    for pay in payData.loc[card]:    #python 中没有switch case

        if pay == -2:
            day2 += 1
            
        elif pay == -1:
            day1 += 1

        elif pay == 0:
            day0 += 1
        else:    
        #if pay > 0  :
            day3 += 1
    
    if day2 == 6:  #6个月都是-2
        paydelay.append(-1)
    elif day1 == 6:  #6个月都是-1
        paydelay.append(0)
    elif day0 == 0 and day3 == 0: #没有0 和逾期记录的
        paydelay.append(-1)
    else :
        if day0 > 0: #有则算一个
            paydelay.append((day3+1)) #'%s'%
        else :    
            paydelay.append( day3) # '%s'%
    
            
#X12-X17  X18-X23 可以构造一个还款能力   和消费能力
#总和相比  还款能力    消费能力是就账单总和  然后两个都标准化 
consumptionLevel = cardData[['BILL_AMT1','BILL_AMT2','BILL_AMT3','BILL_AMT4','BILL_AMT5','BILL_AMT6']]
repaymentAbility = cardData[['PAY_AMT1','PAY_AMT2','PAY_AMT3','PAY_AMT4','PAY_AMT5','PAY_AMT6']]

#消费水平    
consumeLevel = []
for bill in consumptionLevel.index:
    paySum = 0
    for pay in consumptionLevel.loc[bill]:
        paySum += pay
        
    consumeLevel.append(paySum) #'%s'%
    
#还款能力
repayAbility = []
for bill in repaymentAbility.index:
    paySum = 0
    for pay in repaymentAbility.loc[bill]:
        paySum += pay
        
    repayAbility.append(paySum)  #'%s'%

tmp = []    
for pay in np.arange(len(repayAbility)):
    if not consumeLevel[pay] == 0:
        tmp.append( (repayAbility[pay] / consumeLevel[pay]))
    else:
        tmp.append(0)

repayAbility = tmp

df = pd.concat([(pd.DataFrame(cardData,columns=['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE','Y'])),pd.DataFrame(paydelay),pd.DataFrame(consumeLevel),pd.DataFrame(repayAbility)], ignore_index=True, axis=1)
df.columns = ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE','Y','paydelay','consumeLevel','repayAbility']

#对三个数值比较大的做标准化处理  'LIMIT_BAL' 'AGE' 'consumeLevel'
from sklearn.preprocessing import MinMaxScaler 
min_max_scaler = MinMaxScaler(copy = False)
df_minmax = min_max_scaler.fit_transform(df[['LIMIT_BAL','AGE','consumeLevel']])

df.pop('LIMIT_BAL')
df.pop('AGE')
df.pop('consumeLevel')

df = pd.concat([df,pd.DataFrame(df_minmax)], ignore_index=True, axis=1)
df.columns = ['SEX', 'EDUCATION', 'MARRIAGE', 'Y','paydelay','repayAbility','LIMIT_BAL', 'AGE', 'consumeLevel']

X = df[['SEX', 'EDUCATION', 'MARRIAGE','paydelay','repayAbility','LIMIT_BAL', 'AGE', 'consumeLevel']]
Y = df[['Y']]
#构建模型
'''
请仔细阅读上面的数据集说明，完成以下项目要求：
1. 将数据集随机划分为训练集与测试集（70% VS 30%）
2. 请使用logistic regression 建立分类模型
3. 请使用KNN建立分类模型
4. 请使用RandomForest建立分类模型
5. 请使用 AUC-ROC，F1比较上面三个模型
'''


from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test= train_test_split(X,Y,train_size = 0.7,random_state =1)


#logistic regression   
from sklearn.linear_model import LogisticRegression 
## 建模
classifier = LogisticRegression()  # 使用类，参数全是默认的  
classifier.fit(X_train, y_train)  # 训练数据来学习，不需要返回值  
##预测  
y_clas = classifier.predict(X_test) # 测试数据，分类返回标记  


#KNN
from sklearn.neighbors import KNeighborsClassifier
##建模
neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(X_train, y_train) 
##预测
y_neigh = neigh.predict(X_test) # 测试数据，分类返回标记  


#RandomForest
from sklearn.ensemble import RandomForestRegressor

#n_estimators=10,
#max_features='auto', )
    
estimator = RandomForestRegressor(random_state=0, n_estimators=100)
estimator.fit(X_train, y_train)
y_esti = estimator.predict(X_test)


#F1
from sklearn.metrics import f1_score
##求出F1值
#logistic regression  
f1_score(y_test, y_clas, average='macro')  
f1_score(y_test, y_clas, average='micro')  
f1_score(y_test, y_clas, average='weighted')  
f1_score(y_test, y_clas, average=None)
#KNN 
f1_score(y_test, y_neigh, average='macro')  
f1_score(y_test, y_neigh, average='micro')  
f1_score(y_test, y_neigh, average='weighted')  
f1_score(y_test, y_neigh, average=None)
#RandomForest 
f1_score(y_test, y_esti, average='macro')  
f1_score(y_test, y_esti, average='micro')  
f1_score(y_test, y_esti, average='weighted')  
f1_score(y_test, y_esti, average=None)

#AUC-ROC
from sklearn.metrics import roc_auc_score
##logistic regression  
roc_auc_score(y_test, y_clas)

from sklearn.metrics import roc_curve
fpr,tpr,thresholds = roc_curve(y_test,y_clas,pos_label=1) #构建ROC曲线图，pos_label=1表示正类的类别标记 = 1
import matplotlib.pyplot as plt
plt.plot(fpr,tpr,linewidth = 2,label ="ROC of CART")
plt.xlabel("False positive Rate")
plt.ylabel("True positive Rate")
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc =4) #图例及位置


#KNN 
roc_auc_score(y_test, y_neigh)
fpr,tpr,thresholds = roc_curve(y_test,y_clas,pos_label=1) #构建ROC曲线图，pos_label=1表示正类的类别标记 = 1
plt.plot(fpr,tpr,linewidth = 2,label ="ROC of CART")
plt.xlabel("False positive Rate")
plt.ylabel("True positive Rate")
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc =4) #图例及位置

          
#RandomForest 
roc_auc_score(y_test, y_esti)
fpr,tpr,thresholds = roc_curve(y_test,y_clas,pos_label=1) #构建ROC曲线图，pos_label=1表示正类的类别标记 = 1
plt.plot(fpr,tpr,linewidth = 2,label ="ROC of CART")
plt.xlabel("False positive Rate")
plt.ylabel("True positive Rate")
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc =4) #图例及位置