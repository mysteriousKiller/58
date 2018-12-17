# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WubaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 本地服务url
    bendi = scrapy.Field()

    # 公司名称
    gongsi = scrapy.Field()

    #电话
    # dianhua = scrapy.Field()

    # 名称
    mingcheng = scrapy.Field()

    # 描述
    miaoshu = scrapy.Field()

    # URL地址
    lianjie = scrapy.Field()

    # pass
