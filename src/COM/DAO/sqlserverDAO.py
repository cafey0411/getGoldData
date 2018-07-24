import pymssql
from config import dbSettings

class sqlserverDAO:

    def __init__(self):
        print("_ini_===========:")
        pass

    def getConnection(self):
        return pymssql.connect(server=dbSettings.SQLSERVER_HOST,
                               user=dbSettings.SQLSERVER_USER,
                               password=dbSettings.SQLSERVER_PASSWD,
                               database=dbSettings.SQLSERVER_DBNAME,
                               charset=dbSettings.SQLSERVER_ENCODE)


    def ExecOneQuery(self, sql):

        conn = self.getConnection()
        cur = conn.cursor()

        cur.execute(sql)
        conn.commit()
        # 释放数据连接
        if cur:
            cur.close()
        if conn:
            conn.close()

    def ExecManyQuery(self, sql, list):
        conn = self.getConnection()
        cur = conn.cursor()

        cur.executemany(sql, list)  # 批量插入数据
        conn.commit()
        # 释放数据连接
        if cur:
            cur.close()
        if conn:
            conn.close()

