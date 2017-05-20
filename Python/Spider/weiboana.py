# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 03:03:46 2017

@author: Isola
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time #间隔为0.5s


def weibo_spider(url,page,delayTime,fileName):
    headers = {'User-Agent': "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"}   #百度UA
    cookie = {'Cookie':'ALF=1495940966; SCF=AoEt_seSdvL1z9kXQNXHDkevnGOdEim9cSrG8x2XRcIYUKTPXskL9NUPkPZJsfsucoM6acS97yTTdNM_w4hTkio.; SUB=_2A250BsIkDeThGeVO6VMT-C7Jwz2IHXVXCO5srDV6PUJbktBeLUbAkW0GwcaL7jhYhGQpkBiOpoNPlHbZBQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5MddyJ9mrNPr7R-uPRSYJb5JpX5o2p5NHD95Q0ehzpeon7SKnpWs4Dqcj_i--NiKnRiKnci--ciKn4iK.0i--NiKnciKyWi--fi-82i-24i--fi-82iK.7; SUHB=0S7SisJMF3g7UW; SSOLoginState=1493348981; _T_WM=44b2d1dad3f4664cdbbe8289cfa7d65c; M_WEIBOCN_PARAMS=luicode%3D20000174'}
    df = pd.DataFrame() 
        
    for i in range(1,page):
        print('spider page %s' % i)  #页码太多爬的时间太长，可以看爬取状态
        time.sleep(delayTime)
        response = requests.get(url+str(i), headers = headers ,cookies = cookie)
        print(response.status_code)
        if not response.text:
            print ("load page%s fail!" % i) 
            continue
        
        soup = BeautifulSoup(response.text, "html.parser", from_encoding='utf-8')
        #爬取到的格式如下
        #<span class="ctt">我爱你，为了你的幸福，我愿意放弃一切--包括你。     ——张爱玲 &#8203;&#8203;&#8203;</span>
        list_soup = soup.find_all('span', class_ = "ctt")
        nan_list = []
        for sr in list_soup:
            nan_list.append(sr.string)
        
        df = pd.concat([df,pd.DataFrame(nan_list)],axis=0,ignore_index = True)
    
    df.dropna() 
    df.drop_duplicates() #删除所有重复的行 
    df.to_csv("E:\\coding\\Spyder\\spider\\%s.csv"% (fileName))


'''
# 先登录或者 cookies
time.sleep(0.5)
response = requests.get(url+'1', headers=headers,cookies = cookie)
print(response.status_code)
i = 1
if not response.text:
    print ("load page%s fail!" % i) 
    continue

#lxml
web_soup = BeautifulSoup(response.text, "lxml", from_encoding='utf-8') 

# 保存文件
file = open('wulxml.txt','w',encoding = 'utf-8')
file.write(web_soup.prettify())
file.close()

# 加载文件
loadfile = open("E:\\coding\\Spyder\\spider\\ana\\wuhua.txt",encoding = 'utf-8')                      
webData = loadfile.read()
#loadfile.close()

#<input type="submit" value="跳页"/>
good = web_soup.find_all('div', {'value':"跳页"})

#html.parser
web_soup = BeautifulSoup(webData, "html.parser", from_encoding='utf-8')

#<span class="ctt">做比较爽还是咬比较爽？ &#8203;&#8203;&#8203;</span>

wu_list = web_soup.find_all('span',class_ ="ctt")
#web_soup.find_all('div',value = '跳页')


'''


if __name__ == '__main__':
    #url = 'https://weibo.cn/u/5411873901?page='    #名言
    url = 'https://weibo.cn/u/3519854135?page='   #wuhua
    page = 74
    fileName = 'wuhua'
    delayTime = 0.5
    weibo_spider(url,page,delayTime,fileName) #开爬