# -*- coding: utf-8 -*-

#from jdcomment.items import JDgoodsItem
from jdcomment.items import JdcommentItem
from scrapy import Request
from scrapy_redis.spiders import RedisCrawlSpider
# from scrapy.spiders import Spider
from scrapy.selector import Selector
import re

import  json
#import os
##python 2.x
import sys
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")


phone_list_url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&page={}&psort=4'
comment_url_api = ('https://club.jd.com/comment/productPageComments.action?productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0')
num_pat = re.compile('(\d*?)')


# https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&page=70&psort=4
# https://item.jd.com/11728969226.html 
# https://club.jd.com/comment/productPageComments.action?productId=3296831&score=0&sortType=5&page=5000&pageSize=10&isShadowSku=0
# 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&page=%s&psort=4'%(lamdbe page: for page in range(1, 70))
# 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&page={}&psort=4'.format(page for page in range(1, 70))

class JDgoodsSpider(RedisCrawlSpider):
    name = 'jdGoods'
    redis_key = 'jdGoods:start_urls'
    allowed_domains = ['jd.com']
#    start_urls = [phone_list_url.format( page) for page in range(1, 101)] 
    start_urls = [phone_list_url.format(page )for page in range(1, 70) ] 
    
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)
        
    def parse(self, response):
        item_urls = response.xpath('//li[@class="gl-item"]/div')
        for item_xpath in item_urls:
            url = item_xpath.xpath('div[@class="p-img"]/a/@href').extract_first() #default='not-found'
            if not url or 'ccc-x' in url:
                continue
            iid = url[url.rfind('/')+1:-5]
            yield Request(
                comment_url_api.format(iid, 1),
                callback=self.parse_comment,
                meta={'page': 1, 'iid': iid, 'retry': 0})
            
            
    def parse_comment(self, response):
        iid = response.meta['iid']
        page = int(response.meta['page'])
        retry = int(response.meta['retry'])
        try:
            json_data = json.loads(response.text)
        except Exception as e:
            if retry < 10:
                yield Request(
                    comment_url_api.format(iid, page),
                    callback=self.parse_comment,
                    meta={'page': page, 'iid': iid, 'retry': retry+1})
            return
        if not json_data['comments']:
            return
        for cd in json_data['comments']:
            d = {}
            d['_id'] = cd['id']
            d['uid'] = cd['guid']
            d['iid'] = cd['referenceId']
            d['productName'] = cd['referenceName'].strip().replace(' ','').replace(',','')
            d['color'] = cd['productColor'].replace(' ','').replace(',','')
            d['size'] = cd['productSize'].replace(' ','').replace(',','').replace('\n', '')
            d['creation_time'] = cd['creationTime'].replace(' ','').replace(',','')
            d['comment'] = cd['content'].replace('&hellip;','').replace('\n', '').replace(' ','').replace(';','-').replace(',','-')
            d['score'] = cd['score']
            d['days'] = cd['days']
            d['afterDays'] = cd['afterDays']
            d['userClientShow'] = cd['userClientShow'].strip()
            d['userClient'] = cd['userClient']
            d['user_level'] = cd['userLevelName']

            sc = JdcommentItem(d)
            yield sc
        yield Request(
            comment_url_api.format(iid, page+1),
            callback=self.parse_comment,
            meta={'page': page+1, 'iid': iid, 'retry': 0})
