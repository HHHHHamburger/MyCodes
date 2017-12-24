# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdcommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    uid = scrapy.Field()
    iid = scrapy.Field()
    productName = scrapy.Field()
    color = scrapy.Field()
    size = scrapy.Field()
    creation_time = scrapy.Field()
    comment = scrapy.Field()
    score = scrapy.Field()
    days = scrapy.Field()
    afterDays = scrapy.Field()
    userClientShow = scrapy.Field()
    userClient = scrapy.Field()
    user_level = scrapy.Field()



class JDgoodsItem(scrapy.Item):
    goodsId = scrapy.Field()
    commentCount = scrapy.Field()