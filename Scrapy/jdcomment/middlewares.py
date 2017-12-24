# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy import log

class JdcommentSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


__metaclass__ = type
import random
#import base64

from agents import AGENTS
#from .proxies import PROXIES
#        proxy = random.choice(PROXIES)

class RandomUserAgentMiddleware():
    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        if agent:
            #显示当前使用的useragent
            #print("********Current UserAgent:%s************" %agent)
            log.msg('Current UserAgent: '+agent, level=log.INFO)
            request.headers.setdefault('User-Agent', agent)


class ProxyMiddleware():
    @classmethod
    def from_crawler(cls, crawler):
        return cls()
    
    def process_request(self, request, spider):
        f = open('./proxy_list.txt')
        proxy_list = f.readlines()
        f.close()
        rd = random.randint(0, len(proxy_list) - 1)
        proxy_ip = "https://%s" % (proxy_list[rd].strip())
        #proxy_ip = "http://%s" % (proxy_list[rd].strip())
        log.msg('Current proxy_ip: '+proxy_ip, level=log.INFO)
        request.meta['proxy'] =  proxy_ip
                    
        #request.meta['proxy'] = "http://%s" % proxy_ip
        #request.meta['proxy'] =  {'http': "http://%s" % proxy_ip}
        
        
        
        