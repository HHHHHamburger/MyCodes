#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#蒙提霍爾問題

import random  
#import numpy as np     
x = 10000
ret = []   
huan = []  
insist = []  

while(x):
    car = random.randint(1,3)
#    car = 1 #固定不固定  不影响结果
    door = {1,2,3}
#    door = {i for i in range(1,101)}  #
    removnum = []
    
    choice = random.randint(1,3)
    door.remove(choice)
    
    for i in  door:
        if i !=  car :
             removnum.append(i)
    door.remove(random.choice(removnum))
#    for i in random.sample(removnum,98):
#       door.remove(i)
    
    flag = random.randint(1,2)   #随机选择 这里概率会重置
    if flag == 1: #insist   
        #insist.append( car ==  choice)
        ret.append(car ==  choice)    #坚持不换 则成功率是1/3   等于3个里选车的概率
    else :  #huan   
        ret.append(car in door)   #换了的概率等于是1/3的反面  
        #huan.append( car in door) 
        
    insist.append( car ==  choice)    
    huan.append( car in door) 
    print("%s times left"% x) 
    x -=1
    
    
from pandas import Series
s = Series(ret)
h = Series(insist)
c = Series(huan)
print("随机换的概率")
print(s.value_counts(dropna=False))
print("不换的概率")
print(h.value_counts(dropna=False))
print("换的概率")
print(c.value_counts(dropna=False))
