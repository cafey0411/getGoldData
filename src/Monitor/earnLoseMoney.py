
import time
from src.COM.DAO.mysqlPooled import Mysql
import tkinter.messagebox
from config import paraSettings

def alertMonitorData():
    # 实例化对象
    dao = Mysql()

    #设置要监控的值

    #买出价格1
    AgTD_BUY_PRICE_1= paraSettings.AG_SEL_PRICE_1
    #买入手数1
    AGTD_BUY_LOTS_1 = paraSettings.AG_BUY_LOTS_1

    #买出价格2
    AgTD_BUY_PRICE_2= paraSettings.AG_SEL_PRICE_2
    #买入手数2
    AGTD_BUY_LOTS_2 = paraSettings.AG_BUY_LOTS_2

    #买出价格3
    AgTD_BUY_PRICE_3 = paraSettings.AG_SEL_PRICE_3
    #买入手数3
    AGTD_BUY_LOTS_3 = paraSettings.AG_BUY_LOTS_3

    #保证金率
    AGTD_BOND_RATE = paraSettings.AGTD_BOND_RATE

    #查找最新数据中的值
    delsql = "select latest_price from (select latest_price from golddata  order by now_date desc limit 1 ) t "
    #delsql += " where latest_price >='%s' OR latest_price <='%s'" % (monitor_price_high, monitor_price_low)
    #print(delsql)
    print("======%s=======" % time.strftime('%Y-%m-%d %X',time.localtime()))

    last_price = dao.getOne(delsql)[0]
    print("new： %s" % last_price)

    #交易手续费计算
    transactionFees_1 = round((last_price + AgTD_BUY_PRICE_1) * 8 / 10000 * AGTD_BUY_LOTS_1  ,1)
    transactionFees_2 = round((last_price + AgTD_BUY_PRICE_2) * 8 / 10000 * AGTD_BUY_LOTS_2 , 1)
    transactionFees_3 = round((last_price + AgTD_BUY_PRICE_3) * 8 / 10000 * AGTD_BUY_LOTS_3, 1)
    transactionFees_all = round(transactionFees_1 + transactionFees_2  + transactionFees_3,1)
    #print("交易手续费： %s" % transactionFees_all)

    #延期费待计算

    #盈亏计算1
    earnLoseMoney_1 = round( (AgTD_BUY_PRICE_1 - last_price) * AGTD_BUY_LOTS_1 ,1)
    #print("盈亏1： %s" % earnLoseMoney_1)

    #盈亏计算2
    earnLoseMoney_2 = round( (AgTD_BUY_PRICE_2 - last_price) * AGTD_BUY_LOTS_2 ,1)
    #print("盈亏2： %s" % earnLoseMoney_2)

    #盈亏计算3
    earnLoseMoney_3 = round( (AgTD_BUY_PRICE_3 - last_price) * AGTD_BUY_LOTS_3 ,1)
    #print("盈亏3： %s" % earnLoseMoney_3)

    #总盈亏
    earnLoseMoney_all = earnLoseMoney_1 + earnLoseMoney_2  + earnLoseMoney_3
    #print("总盈亏： %s" % earnLoseMoney_all)

    #print("扣除手续费： %s" % (earnLoseMoney_all -transactionFees_all))
#=====================定时执行
def timer(n):
      '''''
      每n秒执行一次
      '''
      while True:
        #print(time.strftime('%Y-%m-%d %X',time.localtime()))
        alertMonitorData() # 此处为要执行的任务
        time.sleep(n)

if __name__=="__main__":
    # 每n秒执行一次
    timeFrequency = paraSettings.MONITOR_TIME_FREQUENCY
    timer(timeFrequency)
