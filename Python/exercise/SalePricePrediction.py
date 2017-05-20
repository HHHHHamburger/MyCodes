# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:14:48 2017
http://www.leiphone.com/news/201704/Py7Mu3TwRF97pWc7.html
@author: Isola
"""

#from pylab import *
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor #随机深林预测模型

test = pd.read_csv('E:\coding\Data\kaggle\\test.csv',encoding = 'GBK')
df_train = pd.read_csv('E:\coding\Data\kaggle\\train.csv',encoding = 'GBK')

test.head(10)
test.columns
test.shape
test.index

#集中学习
#One-Hot Encoding    独热码
OneHotEncoder(sparse = False).fit_transform( testdata['age', 'salary'])

x1 = df_train[['OverallQual','YearBuilt','TotalBsmtSF','GrLivArea']]
y1 = df_train['SalePrice'] 

sns.distplot(y1)

#Grlivarea 与 SalePrice 散点图
var = 'GrLivArea'
data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));

# TotalBsmtSF 与 SalePrice 散点图                 
var = 'TotalBsmtSF'
data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));
                 
#‘OverallQual’与‘SalePrice’箱型图                 
var = 'OverallQual'
data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x=var, y="SalePrice", data=data)
fig.axis(ymin=0, ymax=800000);

#YearBuilt 与 SalePrice 箱型图        
var = 'YearBuilt'
data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
f, ax = plt.subplots(figsize=(16, 8))
fig = sns.boxplot(x=var, y="SalePrice", data=data)
fig.axis(ymin=0, ymax=800000);plt.xticks(rotation=90);

#相关系数矩阵
corrmat = df_train.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True);  
           
           
#SalePrice 相关系数矩阵

k = 10 #number ofvariables for heatmap
cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
cm = np.corrcoef(df_train[cols].values.T)
sns.set(font_scale=1.25)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, 
yticklabels=cols.values, xticklabels=cols.values)
plt.show()


#SalePrice 和相关变量之间的散点图

sns.set()
cols = ['SalePrice', 'OverallQual', 'GrLivArea','GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
sns.pairplot(df_train[cols], size = 2.5)
plt.show();

#缺失值处理     不同的变量根据情况进行不同的处理
#①
total= df_train.isnull().sum().sort_values(ascending=False)
percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total','Percent'])
missing_data.head(20)

df_train= df_train.drop((missing_data[missing_data['Total'] > 1]).index,1)
df_train= df_train.drop(df_train.loc[df_train['Electrical'].isnull()].index)
df_train.isnull().sum().max() #justchecking that there's no missing data missing...

#②
#对于分类特征 
df_train["MasVnrArea"].fillna(0,inplace = True) #使用0来填充NA
all_df["LotFrontage"] = df["LotFrontage"]
for key,group in lot_frontage_by_neighborhoob:
    idx = (df["LotFrontage"]) == key) & (df["LotFrontage"].isnull())
    all_df.loc[idx,"LotFrontage"] = group.median()
    
dumnies = pd.get_dummies(train_df[column_name],prefix = "_"+column_name)

               
#异常值分析
#面积在4000以上的去掉


#构建模型



