#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-
'''
Created on 2017年3月9日
@author: HGladiator
'''
import requests
from bs4 import BeautifulSoup
from contextlib import closing  #自动管理流
import time #间隔为0.5s

def tieba_spider():
    url = 'https://tieba.baidu.com/p/1716787888?pn=' 
    headers = {'User-Agent': "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"}   #百度UA
    f = open('/home/image/img_result.txt', 'w')
    url_set = set()
    for i in range(27,43):
        f.write('page %s'% i)
        #print 'page %s' % i  #页码太多爬的时间太长，可以看爬取状态
        time.sleep(0.5)
        response = requests.get(url+str(i), headers=headers)
        if not response.text:
            print "load page%s fail!" % i
            continue
        soup = BeautifulSoup(response.text, "html.parser", from_encoding='utf-8')
        #爬取到的格式如下
        #<img class="BDE_Image" height="293" src="https://imgsa.baidu.com/forum/w%3D580/sign=3d8e3748912397ddd679980c6983b216/8aeba7efce1b9d16a54c94cef3deb48f8d546447.jpg" width="440">
        list_soup = soup.find_all('img', class_ = "BDE_Image")

        for link in list_soup:
            img_url = link['src']
            if img_url not in url_set:
                url_set.add(img_url)
                img_text = link.get_text().encode('utf-8')   #utf-8略显多余运行会warning
                
                #把结果写到文本中
                f.write(img_url)
                f.write('\n')
                if len(img_text) > 40:
                    #img_text = img_text[:100].strip() 
                    img_text = img_text.decode('utf-8')[:40].encode('utf-8')  #这里先解码取汉字再转码
                f.write(img_text)
                f.write('\n')
                
                #把图片下载下来
                time.sleep(0.5)
                try:
                    with closing(requests.get(img_url, headers=headers, stream=True)) as response:
                        # 打开文件
                        with open('/home/slimane/image/%s.jpg'% img_text, 'wb') as fd:
                            # 每128写入一次
                            for chunk in response.iter_content(128):
                                fd.write(chunk)
                except Exception as e:
                    print e
                    # print "key doesn't exist"
                
    f.close()

if __name__ == '__main__':
    '''
    开爬
    '''
    tieba_spider()
