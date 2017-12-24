# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
#import time
#import socket
#import select
#import sys
import os
import re
#import errno 
import json
import codecs
import redis

from jdcomment.items import JdcommentItem


class JdcommentPipeline(object):
    r = redis.Redis(host='106.75.136.128', port=6379)
    def process_item(self, item, spider):
        for i in range(0, self.r.llen('Search:items'), 100):
            items = self.r.lrange('Search:items', start=0, end=100)
        return items


val_indices = {'_id': 0, 'uid': 1, 'iid': 2, 'productName': 3, 'color': 4,
               'size': 5, 'creation_time': 6, 'user_level': 7, 'score': 8,
               'days':9,'afterDays':10,"userClientShow":11,'userClient':12,'comment':13}


class phoneCommentPipeline(object):
    seen_ids = set()

    @classmethod
    def from_crawler(cls, crawler):
        pipe = cls()
        if not os.path.exists('jd_phone_comments.csv'):
            return pipe
        pat = re.compile('^\d+?,')
        with open('jd_phone_comments.csv', 'r') as f:
            for line in f:
                _id = pat.findall(line)
                if _id:
                    pipe.seen_ids.add(_id[0])
        return pipe

    def process_item(self, item, spider):
        if not isinstance(item, JdcommentItem):
            return item

        _id = item['_id']
        if _id in self.seen_ids:
            raise DropItem('{} Have been processed.'.format(_id))
        self.seen_ids.add(_id)

        key_values = list(item.items())
        key_values.sort(key=lambda x: val_indices[x[0]])
        values = [str(val) for key, val in key_values]
        with open('jd_phone_comments.csv', 'a') as f:
            f.write(','.join(values)+'\n')
        return item