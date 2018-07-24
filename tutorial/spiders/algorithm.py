# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from scrapy.loader import ItemLoader
from tutorial.items import GoldData

#爬取马克威算法图标
#CREATE 20170622 QJL
class AlgorithmSpider(scrapy.Spider):
    name = "algorithm"
    allowed_domains = ["sge.com.cn"]
    start_urls = (
        'http://www.sge.com.cn/sjzx/yshqbg',
       # 'http://www.markwaymall.com/Index/algorithm.html',
    )

    def parse(self, response):

        # sel = Selector(response)
        # seltmp = sel.xpath("//div[@class='wrap_little_banner']/div/a[2]/@href").extract()

        # #针对此网页入口被禁掉时
        request = scrapy.Request('http://www.sge.com.cn/sjzx/yshqbg', callback=self.parse_item)
        yield request

        # next_full_url = Selector(response)
        # for link in next_full_url.xpath("//div[@class='wrap_container']/div/ul[@class='content']/li/a/@href").extract():
        #     #记得要加上：http://www.markwaymall.com/
        #     request = scrapy.Request('http://www.markwaymall.com/%s' % link, callback=self.parse_item)
        #     #print("======yield request======:"+link)
        #     yield request

    def parse_item(self, response):
        l = ItemLoader(item=GoldData(), response=response)
        l.add_xpath('date', "//html/body/div[6]/div/div[2]/div[2]/div[2]/div[1]/p/span[2]/text()")


        l.add_xpath('contract_name', "//td/text()")
        l.add_xpath('latest_price', "//span[@class='colorRed' or @class='colorGreen' or @class='']/text()")
        return l.load_item()  #当返回items时候会被pipelines调用
