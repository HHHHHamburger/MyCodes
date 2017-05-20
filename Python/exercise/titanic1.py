# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:40:16 2017

@author: Isola
"""

'''
PassengerId：乘客序号；
Survived：最终是否存活（1表示存活，0表示未存活）；
Pclass：舱位，1是头等舱，3是最低等；
Name：乘客姓名；
Sex：性别；
Age：年龄；
SibSp：一同上船的兄弟姐妹或配偶；
Parch：一同上船的父母或子女；
Ticket：船票信息；
Fare：乘客票价，决定了Pclass的等级；
Cabin：客舱编号，不同的编号对应不同的位置；
Embarked：上船地点，主要是S（南安普顿）、C（瑟堡）、Q（皇后镇）
'''


#①
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os 


os.chdir('E:\\coding\\Spyder\\exercise\\titanic')
train = pd.read_csv('.\\train.csv', header = 0,encoding = 'utf-8')
test = pd.read_csv('.\\test.csv', header = 0,encoding = 'utf-8')
#data = data.dropna() #去除缺失

                   
train.describe()
train.head()
train.shape
test.shape

train.info()

train["Survived"].value_counts()  #看一下死活数

#简单统计男女比例	
sns.factorplot('Sex',data=train,kind="count")


#我们显示以Pclass作为X轴，统计每个等级中的男女比例
sns.factorplot('Pclass',data=train,kind="count",hue="Sex")


#定义一个函数，判断男，女，小孩
def male_famle_child(passenger):
    age,sex = passenger
     
    if age < 16:
        return "Child"
    else:
        return sex

###新增一字段“Person”

train["Person"] = train[["Age","Sex"]].apply(male_famle_child,axis=1)

#再次在Pclass分类中体现男女小孩的比例
sns.factorplot("Pclass",data=train,hue="Person",kind="count")

#简要查看各年龄段的发布，将年龄段的间距分为70段，默认10段
train['Age'].hist(bins=70)

#查看平均年龄：
train["Age"].mean()

#查看“Person”字段的数量统计
titanic_df["Person"].value_counts()


#统计不同年龄段，个类别的分布趋势，核密度统计方式
fig = sns.FacetGrid(titanic_df,hue="Sex",aspect=4)   
###使用map函数映射kde，以Age作为X轴
fig.map(sns.kdeplot,"Age",shade=True)
###取最大年龄
oldest = titanic_df["Age"].max()
###设置x轴的取值范围为0到oldest
fig.set(xlim=(0,oldest))
###添加图标，印记
fig.add_legend()


fig = sns.FacetGrid(titanic_df,hue="Person",aspect=4)
fig.map(sns.kdeplot,"Age",shade=True)
oldest = titanic_df["Age"].max()
fig.set(xlim=(0,oldest))
fig.add_legend()

fig = sns.FacetGrid(titanic_df,hue="Pclass",aspect=4)
fig.map(sns.kdeplot,"Age",shade=True)
oldest = titanic_df["Age"].max()
fig.set(xlim=(0,oldest))
fig.add_legend()

#统计不同船舱的人数分布
#首先取得不同船舱的等级
deck = titanic_df["Cabin"].dropna()   ##去掉NaN的值
deck.head()

#船舱的类别由第一个字符可以加以区分可以得到各船舱人数的数量
levels = []
for level in deck:
    levels.append(level[0])
     
cabin_df = DataFrame(levels)
cabin_df.columns = ["Cabin"]    ###为序列加上字段名

                   
sns.factorplot("Cabin",data=cabin_df,palette="winter_d",kind="count")



#因为上面T船舱的数量实在太小，酌情删除
cabin_df = cabin_df[cabin_df.Cabin != "T"]
#然后生成图片
sns.factorplot("Cabin",data=cabin_df,palette="summer",kind="count")

#统计进站港口的数量分布
sns.factorplot("Embarked",data=titanic_df,hue="Pclass",
x_order=["C","Q","S"]
,kind="count")

#统计单身及有家庭的人数分布
###创建Alone字段
titanic_df["Alone"] = titanic_df.SibSp + titanic_df.Parch
titanic_df["Alone"]

###由上可知，大于1的都是有兄弟姐妹或者父母孩子的
###所以修改Alone字段的数字为Alone或者with family
titanic_df["Alone"].loc[titanic_df["Alone"] > 0] ="With Family"
titanic_df["Alone"].loc[titanic_df["Alone"] == 0] = "Alone"
titanic_df.head()

#查看alone人数
sns.factorplot("Alone",data=titanic_df,hue="Pclass",palette="Blues",kind="count")


#统计存活的以及没存活的分布
##简单将Survivor字段的0,1映射成no与yes，及没有存活及存活
titanic_df["Survivor"] = titanic_df.Survived.map({0:"no",1:"yes"})
sns.factorplot("Survivor",data=titanic_df,palette="Set1",kind="count")

#注意：factoryplot函数第一个值取X轴，第二个值为Y轴
sns.factorplot("Pclass","Survived",data=titanic_df,x_order=[1,2,3])
#再次使用一个因素图，但现在考虑阶级和性别
sns.factorplot('Pclass','Survived',hue='person',data=titanic_df)
#使用线性图对年龄与生存
sns.lmplot('Age','Survived',data=titanic_df)

#线性图的年龄与生存使用色相的类分离
sns.lmplot('Age','Survived',hue='Pclass',data=titanic_df,palette='winter')


generations=[10,20,40,60,80]
sns.lmplot('Age','Survived',hue='Pclass',data=titanic_df,palette='winter',x_bins=generations)

sns.lmplot('Age','Survived',hue='Sex',data=titanic_df,palette='winter',x_bins=generations)