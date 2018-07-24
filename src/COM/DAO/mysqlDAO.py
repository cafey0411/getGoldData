import pymysql  #LINUX也支持

from config import dbSettings

class mysqlDAO:

    def __init__(self):
        pass

    def getConnection(self):
        return pymysql.connect(
                              host=dbSettings.MYSQL_HOST,
                              port=dbSettings.MYSQL_PORT,
                              user=dbSettings.MYSQL_USER,
                              passwd=dbSettings.MYSQL_PASSWD,
                              db=dbSettings.MYSQL_DBNAME,
                              charset=dbSettings.MYSQL_ENCODE
                              #,cursorclass=DictCursor
                              )

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

