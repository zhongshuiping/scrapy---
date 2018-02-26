# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BokeyuanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    post_view_count = scrapy.Field()
    post_comment_count = scrapy.Field()
    url = scrapy.Field()

