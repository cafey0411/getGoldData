# -*- coding: utf-8 -*- import sys, locale
#from scrapy import cmdline
import datetime
import time
import os

#cmdline.execute("scrapy crawl algorithm ".split())


import sched
#初始化sched模块的scheduler类
#第一个参数是一个可以返回时间戳的函数，第二个参数可以在定时未到达之前阻塞。
schedule = sched.scheduler ( time.time, time.sleep )

#被周期性调度触发的函数
def func():

    #指定时间内运行==========================================================START
    bridgetime = time.strftime("%Y-%m-%d ")#时间随便定，
    nowtime = bridgetime + time.strftime("%X")

    #AM
    starttime_AM = bridgetime + "9:00:00"
    endtime_AM =  bridgetime + "11:31:00"
    flag1 = Checktime_YMDHMS(starttime_AM,endtime_AM,nowtime)

    #PM
    starttime_PM = bridgetime + "13:30:00"
    endtime_PM =  bridgetime + "15:31:00"
    flag2 = Checktime_YMDHMS(starttime_PM,endtime_PM,nowtime)

    #PM2
    starttime_PM2 = bridgetime + "20:00:00"
    #后一天
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    n_days = now + delta
    endtime_PM2 =  n_days.strftime("%Y-%m-%d ") + "02:31:00"
    flag3 = Checktime_YMDHMS(starttime_PM2,endtime_PM2,nowtime)

    if flag1 == "in" or flag2 == "in" or flag3 == "in":
        # 指定时间内运行==========================================================END
        os.system("scrapy crawl algorithm ")

def perform1(inc):
    schedule.enter(inc,0,perform1,(inc,))
    func()    # 需要周期执行的函数


def mymain():
    schedule.enter(0,0,perform1,(60,))  #每隔60秒


#判断时间是不是落在里面
def Checktime_YMDHMS(starttime, endtime, nowTime):
    Flag='null'
    starttime=time.strptime(starttime,'%Y-%m-%d %H:%M:%S')
    endtime=time.strptime(endtime,'%Y-%m-%d %H:%M:%S')
    #星期几
    whatday = int(datetime.datetime.strptime(nowTime, '%Y-%m-%d %H:%M:%S').strftime("%w"))

    nowTime = time.strptime(str(nowTime), '%Y-%m-%d %H:%M:%S')
    #排除周六日
    if whatday != 6 and whatday != 0:
        if int(time.mktime(endtime)) < int(time.mktime(nowTime)):
            Flag='after'
        elif int(time.mktime(starttime))<= int(time.mktime(nowTime)) and int(time.mktime(endtime))>=int(time.mktime(nowTime)):
            Flag='in'
        elif int(time.mktime(starttime)) > int(time.mktime(nowTime)):
            Flag='before'
    else:
        print("周末休息！")
    return Flag

if __name__=="__main__":
    mymain()
    schedule.run()  # 开始运行，直到计划时间队列变成空为止
