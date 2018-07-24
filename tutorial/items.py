# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class GoldData(scrapy.Item):
    date = scrapy.Field()
    contract_name = scrapy.Field()  #所有表格
    latest_price = scrapy.Field()
    # high_price = scrapy.Field()
    # low_price = scrapy.Field()
    # open_price =scrapy.Field()

