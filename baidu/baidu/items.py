# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    linkmd5id   = scrapy.Field()
    imgid       = scrapy.Field()#图片id
    title       = scrapy.Field()#
    imgsize     = scrapy.Field()
    filesize    = scrapy.Field()
    frame       = scrapy.Field()
    hoverURL    = scrapy.Field()
    thumbURL    = scrapy.Field()
    middleURL   = scrapy.Field()
    fromURLHost = scrapy.Field()
    objURL      = scrapy.Field()
    updateTime  = scrapy.Field()
    tag                     = scrapy.Field()
    category                = scrapy.Field()
    fromURL                 = scrapy.Field()
    source_thumb_url        = scrapy.Field()
    source_original_url     = scrapy.Field()
    description             = scrapy.Field()
    frame                   = scrapy.Field()
    author                  = scrapy.Field()
    isSync                  = scrapy.Field()
    sync_time               = scrapy.Field()
    scrawl_time             = scrapy.Field()
    customer_exceptions     = scrapy.Field()