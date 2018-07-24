
import time
import os
from src.COM.DAO.mysqlPooled import Mysql
import tkinter.messagebox
from config import paraSettings

def show_messagebox(last_price):
    tkinter.messagebox.askokcancel("FishC Demo", '达到设定的值 %s' % last_price)

def alertMonitorData():
    # 实例化对象
    dao = Mysql()

    #设置要监控的值
    monitor_price_high = paraSettings.MONITOR_LATEST_PRICE_HIGH
    monitor_price_low = paraSettings.MONITOR_LATEST_PRICE_LOW
    #查找最新数据中是否有符合设置的值出现 
    delsql = "select latest_price from (select latest_price from golddata  order by now_date desc limit 1 ) t "
    delsql += " where latest_price >='%s' OR latest_price <='%s'" % (monitor_price_high, monitor_price_low)
    #print(delsql)
    if dao.getOne(delsql) != False:
        last_price = dao.getOne(delsql)[0]
        show_messagebox(last_price)
        print(last_price)



#=====================定时执行
def timer(n):
      '''''
      每n秒执行一次
      '''
      while True:
        print(time.strftime('%Y-%m-%d %X',time.localtime()))
        alertMonitorData() # 此处为要执行的任务
        time.sleep(n)


if __name__=="__main__":
    # 每n秒执行一次
    timeFrequency = paraSettings.MONITOR_TIME_FREQUENCY
    timer(timeFrequency)
