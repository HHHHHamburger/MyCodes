# -*- coding:utf-8 -*-
'''by sudo rm -rf http://imchenkun.com'''
import scrapy
from douban.items import DoubanBookItem
 
 
class BookSpider(scrapy.Spider):
    name = 'doubanbook'
    allowed_domains = ['douban.com']
    start_urls = [
        'https://book.douban.com/top250'
    ]
 
    def parse(self, response):
        # 请求第一页
        self.log('A response from %s just arrived!' % response.url)
        yield scrapy.Request(response.url, callback=self.parse_next)
 
        # 请求其它页
        for page in response.xpath('//div[@class="paginator"]/a'):
            link = page.xpath('@href').extract()[0]   #[0]把list变成字符串 可以去重，不知道为啥
            yield scrapy.Request(link, callback=self.parse_next)
 
    def parse_next(self, response):
        for item in response.xpath('//tr[@class="item"]'):
            book = DoubanBookItem()
            book['name'] = item.xpath('td[2]/div[1]/a/@title').extract()[0]
            book['price'] = item.xpath('td[2]/p/text()').extract()[0]
            book['ratings'] = item.xpath('td[2]/div[2]/span[2]/text()').extract()[0]
            yield book
