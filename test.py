
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


    bridgetime = "2018-02-24 "
    starttime = bridgetime + "15:04:15"
    endtime =  bridgetime + "15:34:15"
    nowtime = bridgetime + time.strftime("%X")
    flag = Checktime_YMDHMS(starttime,endtime,nowtime)
    print("Checktime_YMDHMS: %s %s %s %s " % (starttime,endtime,nowtime,flag))