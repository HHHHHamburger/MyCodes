# -*- coding: utf-8 -*-

from jdcomment.items import JdcommentItem
from scrapy import Request
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.selector import Selector
import re

import  json
# import os
# python 2.x
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
# python 3.x
# import importlib,sys
# importlib.reload(sys)
# sys.setdefaultencoding("utf-8")

phone_cates = ['华为','小米','Apple','三星','魅族','锤子','一加','vivo','努比亚','OPPO',
'360','苹果','中兴','乐视','美图','诺基亚','金立','索尼','酷派','ZUK','联想','HTC','飞利浦']


phone_list_url = 'https://search.jd.com/Search?keyword={}&enc=utf-8&page={}'
comment_url_api = ('https://club.jd.com/comment/productPageComments.action?productId={}&score=0&sortType=5&page={}&pageSize=10&isShadowSku=0')
num_pat = re.compile('(\d*?)')


# https://search.jd.com/Search?keyword=Apple&enc=utf-8&page=1
# https://item.jd.com/11728969226.html 
# https://item.jd.com/3355175.html
# https://club.jd.com/comment/productPageComments.action?productId=3355175&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0


class PhoneSpider(RedisCrawlSpider):
    name = 'phone'
    redis_key = 'phone:start_urls'
    allowed_domains = ['jd.com']
    start_urls = [phone_list_url.format(cate, page) for cate in phone_cates
                  for page in range(1, 101)]
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
            d['comment'] = cd['content'].replace('\n', '').replace(' ','')
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