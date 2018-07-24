# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from src.COM.DAO.mysqlPooled import Mysql
import time


class ImageDownloadPipeline(object):
    #处理每一个IMTE（多次调用）
    def process_item(self, item, spider):

        # 存AU99.99
        #self._conditional_insert_au9999(item['date'][0], item['contract_name'],item['latest_price'])
        # 存AU(T+D)
        #self._conditional_insert_autd(item['date'][0], item['contract_name'],item['latest_price'])

        # 存Ag(T+D)
        self._conditional_insert_agtd(item['date'][0], item['contract_name'],item['latest_price'])
        return item

    #存AU99.99
    def _conditional_insert_au9999(self, date, table_data,latest_price):
        # 实例化对象
        dao = Mysql()

        now_time = time.strftime("%Y-%m-%d %X")
        sql = "insert into GoldData_au9999 (date, contract_name, latest_price,high_price,low_price,open_price,now_date) "
        sql += " values('%s','%s','%s','%s','%s','%s','%s')"
        params = (
        str(date), str(table_data[0]), latest_price[0], table_data[1], table_data[2], table_data[3], str(now_time))
        print (sql % params)
        dao.insertOne(sql % params, None)

        # 释放资源
        dao.dispose()

    #存AU(T+D)
    def _conditional_insert_autd(self, date, table_data,latest_price):
        # 实例化对象
        dao = Mysql()

        now_time = time.strftime("%Y-%m-%d %X")
        sql = "insert into GoldData_autd (date, contract_name, latest_price,high_price,low_price,open_price,now_date) "
        sql += " values('%s','%s','%s','%s','%s','%s','%s')"
        params = (
        str(date), str(table_data[20]), latest_price[5], table_data[21], table_data[22], table_data[23], str(now_time))
        print (sql % params)
        dao.insertOne(sql % params, None)

        # 释放资源
        dao.dispose()


    #存Ag(T+D)
    def _conditional_insert_agtd(self, date, table_data,latest_price):
        # 实例化对象
        dao = Mysql()

        now_time = time.strftime("%Y-%m-%d %X")
        sql = "insert into golddata (date, contract_name, latest_price,high_price,low_price,open_price,now_date) "
        sql += " values('%s','%s','%s','%s','%s','%s','%s')"
        params = (
        str(date), str(table_data[16]), latest_price[4], table_data[17], table_data[18], table_data[19], str(now_time))

        print (sql % params)
        dao.insertOne(sql % params, None)

        # 释放资源
        dao.dispose()