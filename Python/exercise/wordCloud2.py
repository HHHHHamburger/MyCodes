# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:31:34 2017

@author: Isola
"""

import pandas as pd
import numpy as np
import jieba
import matplotlib.pyplot as plt

from wordcloud import WordCloud , STOPWORDS#, ImageColorGenerator
#import os 
from os import  chdir


# 读取数据
chdir('E:\\coding\\Spyder\\exercise')
data = pd.read_csv( '.\\jd_comment.csv', header = 0,encoding = 'gb18030')
data = data.dropna() #去除缺失
## 文本去重
# 使用drop_duplicates
data = data.drop_duplicates()
# 统计描述
data.describe()
data.shape

#摘前1W行
data_5w = data.loc[0:50000]  #,['评论']


# 使用unique
#dat_uni = data[0].unique()
## 结巴分词
dat_fc = []
for i in data_5w.index:
    a = list(jieba.cut(data_5w.loc[i,'评论']))   #data.loc[i,'评论'])
    #for x in jieba.cut(data_5w.loc[i]):  #data.loc[i,'评论'])
        #print(x)
    dat_fc.append(a)
#词频统计


#df = pd.DataFrame.from_dict(cnt, {'index','columns'})
#df = pd.DataFrame(cnt, columns = {'Key','Value'})
#comment = pd.Series(dat_fc).value_counts()

#设置阀值  过滤词频低的
## 停用词过滤
# 导入停用词词库
stop_word = pd.read_table('stopwords.txt', sep = '\s+', encoding = 'utf-\
8',header = None, engine='python')
stop = list(stop_word[0])
stop = [' ',''] + stop
           
#cnt = Counter()
#for lit in dat_fc:
#    for word in lit:
#        cnt[word] += 1
           
# 过滤停用词
comment_word = []
for x in dat_fc:
    a = [i for i in x if i not in stop]
    comment_word.append(a)
       
#情感分析


neg_word = pd.read_table('negative.txt', sep = '\s+', encoding = 'utf-\
8',header = None, engine='python')
neg = list(neg_word[0])
pos_word = pd.read_table('positive.txt', sep = '\s+', encoding = 'utf-\
8',header = None, engine='python')
pos = list(pos_word[0])


comment_neg = []
comment_pos = []

for x in comment_word:
    #k = -len([x for x in i if x in neg])
    a = [i for i in x if i  in neg]
    comment_neg.append(a)

for x in comment_word:
    #k = -len([x for x in i if x in neg])
    a = [i for i in x if i  in pos]
    comment_pos.append(a)

#展开
from functools import reduce
#a = reduce(lambda x,y:x+y,comment_word)
pos_text = reduce(lambda x,y:x+y,comment_pos)
neg_text = reduce(lambda x,y:x+y,comment_neg)
#统计词频
from collections import Counter
poscnt  = Counter(pos_text)
negcnt  = Counter(neg_text)

#过滤低频词
poscnt_10 = {k:v for k,v in poscnt.items() if v > 10  }  #and k not in stop
negcnt_10 = {k:v for k,v in negcnt.items() if v > 50 }  #and k not in stop


#neg_text = ''
#for lst in comment_neg:
#    neg_text  += ','.join(lst)
#    
#pos_text = []
#for lst in comment_pos:
#    pos_text  += ','.join(lst) +','

#a = pd.DataFrame(comment_pos)
#comment_pos = comment_pos.dropna() #去除缺失
#comment_neg = comment_neg.dropna() #去除缺失
#comment_word = comment_word.dropna() #去除缺失

# 画词云
wc = WordCloud(font_path='E:\\Swap\\font\\思源宋体简体中文\\NotoSerifCJKsc-Black.otf',#设置字体
            background_color="black", #背景颜色
            max_words=2000,# 词云显示的最大词数
            # mask=back_coloring,#设置背景图片
            max_font_size=40, #字体最大值
            random_state=42,
            #stopwords = set(stop)
            )


# 显示




#wc_neg = wc.generate(negcnt_10)   
#wc_pos = wc.generate(poscnt_10)  #pos_text 
##wc_pos = wc.generate(comment_word)
wc_neg =wc.generate_from_frequencies(negcnt_10)  ##????
wc_pos =wc.generate_from_frequencies(poscnt_10)
plt.figure(figsize=(20,20))
plt.subplot(121)
plt.imshow(wc_neg)

plt.subplot(122)
plt.imshow(wc_pos)
plt.axis("off")

plt.show()
# 图片存储
wc.to_file("a_new_pic.png")



from gensim import corpora, models

#正面主题分析
#pos_comment = pd.Series(comment_word)
#pos_ser = pd.Series(pos_text)
pos_dict = corpora.Dictionary(pos_text)   #pos_word.iloc[:,0]
pos_corpus = [pos_dict.doc2bow(i) for i in pos_text]
pos_lda = models.LdaModel(pos_corpus, num_topics = 3, id2word = pos_dict)
pos_topics = pos_lda.show_topics()#展示主题


pos_dict = corpora.Dictionary(comment_pos)   #pos_word.iloc[:,0]
pos_corpus = [pos_dict.doc2bow(i) for i in comment_pos]
pos_lda = models.LdaModel(pos_corpus, num_topics = 3, id2word = pos_dict)
pos_topics = pos_lda.show_topics()#展示主题


#负面主题分析
pos_dict = corpora.Dictionary(neg_word.iloc[:,0])  #
pos_corpus = [pos_dict.doc2bow(i) for i in neg_word.iloc[:,0]]
pos_lda = models.LdaModel(pos_corpus, num_topics = 3, id2word = pos_dict)
pos_topics = pos_lda.show_topics()#展示主题                                
                                
                                
                                
                                
                        
                                
                                
                                
                                
                                
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname('__file__')
# Read the whole text.
text = open(path.join(d, 'alice.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords)
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "alice.png"))

# show
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()