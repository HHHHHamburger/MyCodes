# 直接爬取
from urllib.request import urlopen
html = urlopen("http://shenzhen.lashou.com/cate/meishi")

# 
from urllib.request import urlopen
from urllib.request import Request

# 网址
url = "http://shenzhen.lashou.com/cate/meishi"
# 请求头
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/56.0.2924.18 Safari/537.36'}
request = Request(url = url, headers = headers)
webData = urlopen(request)
data = webData.read().decode('utf-8')

# 保存文件
file = open('lashou.txt','w')
file.write(data)
file.close()

# 加载文件
loadfile = open("lashou.txt")                      
webData = loadfile.read()

# 数据提取 利用正则表达式

#只返回括号内容
import re
goods_place = re.findall("class=\"goods-place\">(.+)</span>", webData) 
goods_name = re.findall('class="goods-name".+?title(.+?)>(.+?)</a>', webData)
goods_text = re.findall('class="goods-text".+?title.+?>(.+?)</a>', webData)
goods_price = re.findall('class="price".+?</em>(\d+?|\d+?\.\d+?)</span>', webData)
goods_orgPrice = re.findall('class="money".+?<del>(\d+?|\d+?\.\d+?)</del>', webData)

# 数据整理
import pandas as pd
df_goods_name = pd.DataFrame(goods_name)
df_goods_place = pd.DataFrame(goods_place)
df_goods_text = pd.DataFrame(goods_text)
df_goods_price = pd.DataFrame(goods_price)
df_goods_orgPrice = pd.DataFrame(goods_orgPrice)
# 合并数据
result = pd.concat([df_goods_name, df_goods_place, df_goods_text, df_goods_price, df_goods_orgPrice], axis=1, ignore_index = True)
# 合并的下一种写法效果相同
# result = pd.merge(df_goods_name,df_goods_place,left_index=True,right_index=True,how='outer')
result.columns = ['goods_name','goods_place','goods_text','goods_price','goods_orgPrice']

# 数据存储
result.to_csv('D:/Work/train_python/lashou/data/lashouData.csv')


# 利用bs4库进行数据整理
# 加载文件
loadfile = open("../lashou.txt")                      
webData = loadfile.read()

from bs4 import BeautifulSoup
web_soup = BeautifulSoup(webData, 'lxml')
# 获取数据
goods_place = web_soup.find_all('span', {"class":"goods-place"})
goods_name = web_soup.find_all('a', {"class":"goods-name"})
goods_text = web_soup.find_all('a', {"class":"goods-text"})
goods_price = web_soup.find_all('span', {"class":"price"})
goods_orgPrice = web_soup.find_all('span', {"class":"money"})

import pandas as pd
# 把记录保存为DataFrame格式
df_goods_place = pd.DataFrame()
for context in goods_place:
    df_goods_place = pd.concat([df_goods_place, pd.DataFrame([context.get_text(strip=True)])], ignore_index = True)

df_goods_name = pd.DataFrame()
for context in goods_name:
    df_goods_name = pd.concat([df_goods_name, pd.DataFrame([context.get_text(strip=True)])], ignore_index=True)

df_goods_text = pd.DataFrame()
for context in goods_text:
    df_goods_text = pd.concat([df_goods_text, pd.DataFrame([context.get_text(strip=True)])], ignore_index=True)

df_goods_price = pd.DataFrame()
for context in goods_price:
    df_goods_price = pd.concat([df_goods_price, pd.DataFrame([context.get_text(strip=True)])], ignore_index=True)    
    
df_goods_orgPrice = pd.DataFrame()
for context in goods_orgPrice:
    df_goods_orgPrice = pd.concat([df_goods_orgPrice, pd.DataFrame([context.get_text(strip=True)])], ignore_index=True)  

# 合并    
df_result = pd.concat([df_goods_name, df_goods_text, df_goods_place, df_goods_price, df_goods_orgPrice], axis=1, ignore_index=True)    
df_result.columns = ['goods_name','goods_text','goods_place','goods_price','goods_orgPrice']

# 数据存储
df_result.to_csv('D:/Work/train_python/lashou/data/lashouData_1.csv')
