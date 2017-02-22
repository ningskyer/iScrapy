# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HuxiuItem(scrapy.Item):
    """虎嗅网新闻Item"""
    title = scrapy.Field()      # 标题
    link = scrapy.Field()       # 链接
    url = scrapy.Field()       # 链接
    body = scrapy.Field()       # 链接
    source_site = scrapy.Field()       # 链接
    desc = scrapy.Field()       # 简述
    published = scrapy.Field()  # 发布时间