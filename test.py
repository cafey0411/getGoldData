import datetime
import time




def Checktime_YMDHMS(starttime,endtime,weibotime):
    Flag='null'
    starttime=time.strptime(starttime,'%Y-%m-%d %H:%M:%S')
    endtime=time.strptime(endtime,'%Y-%m-%d %H:%M:%S')
    weibotime=time.strptime(str(weibotime),'%Y-%m-%d %H:%M:%S')
    if int(time.mktime(endtime)) < int(time.mktime(weibotime)):
        Flag='after'
    elif int(time.mktime(starttime))<= int(time.mktime(weibotime)) and int(time.mktime(endtime))>=int(time.mktime(weibotime)):
        Flag='in'
    elif int(time.mktime(starttime)) > int(time.mktime(weibotime)):
        Flag='before'
    return Flag

if __name__=="__main__":
    # starttime = "2018-02-24 14:04:15"
    # endtime =  "2018-02-27 14:04:15"
    # nowtime = time.strftime("%Y-%m-%d %X")
    # flag = Checktime_YMDHMS(starttime,endtime,nowtime)
    # print("Checktime_YMDHMS: %s %s %s %s " % (starttime,endtime,nowtime,flag))

    bridgetime = time.strftime("%Y-%m-%d ")#时间随便定，
    # nowtime = bridgetime + time.strftime("%X")
    #
    # #AM
    # starttime_AM = bridgetime + "9:00:00"
    # endtime_AM =  bridgetime + "11:31:00"
    # flag1 = Checktime_YMDHMS(starttime_AM,endtime_AM,nowtime)
    #
    # #PM
    # starttime_PM = bridgetime + "13:30:00"
    # endtime_PM =  bridgetime + "15:31:00"
    # flag2 = Checktime_YMDHMS(starttime_PM,endtime_PM,nowtime)
    #
    # #PM2
    # starttime_PM2 = bridgetime + "20:00:00"
    # endtime_PM2 =  bridgetime + "23:59:00"

    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    n_days = now + delta
    print(n_days.strftime('%Y-%m-%d'))


