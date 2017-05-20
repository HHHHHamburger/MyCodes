# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 16:40:16 2017

@author: Isola
"""

import pandas as pd
import numpy as np
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud  #, STOPWORDS, ImageColorGenerator
#class sklean

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



# 读取数据
data = pd.read_table('..//meidi.txt', header = None)
data = data.dropna() #去除缺失
# 统计描述
data.describe()
## 文本去重
# 使用drop_duplicates
dat_drop = data.drop_duplicates()
# 使用unique
dat_uni = data[0].unique()
## 结巴分词
dat_fc = []
for i in dat_drop.index:
    a = list(jieba.cut(dat_drop.loc[i,0]))
    dat_fc.append(a)
## 停用词过滤
# 导入停用词词库
stop_word = pd.read_table('..//stopwords.txt', sep = '\s+', encoding = 'utf-\
8',header = None, engine='python')
stop = list(stop_word[0])
stop = [' ',''] + stop
# 过滤停用词
comment_word = []
for x in dat_fc:
    a = [i for i in x if i not in stop]
    comment_word.append(a)
# 画词云
wc = WordCloud(font_path='E:\\Swap\\font\\思源宋体简体中文\\NotoSerifCJKsc-Black.otf',#设置字体
            background_color="black", #背景颜色
            max_words=2000,# 词云显示的最大词数
            # mask=back_coloring,#设置背景图片
            max_font_size=40, #字体最大值
            random_state=42,
            )

# 显示
pos_text = ''
for lst in comment_word:
    pos_text  += ','.join(lst)
    
wc_pos = wc.generate(pos_text)

#wc_pos = wc.generate(comment_word)
plt.figure()
plt.imshow(wc_pos)
plt.axis("off")
plt.show()
# 图片存储
wc.to_file("a_new_pic.png")


