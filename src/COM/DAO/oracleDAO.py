import cx_Oracle
from config import dbSettings

class oracleDAO:

    def __init__(self):
        pass

    def getConnection(self):
        return cx_Oracle.connect(
                                user=dbSettings.ORACLE_USER,
                                password=dbSettings.ORACLE_PASSWD,
                                dsn=dbSettings.ORACLE_DSN)

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

