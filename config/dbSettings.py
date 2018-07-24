# -*- coding: utf-8 -*-

#Mysql数据库的配置信息
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'spider'         #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改
MYSQL_PASSWD = '123456'         #数据库密码，请修改
MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用
MYSQL_ENCODE = 'utf8'          #编码要加上，否则可能出现中文乱码问题

#Sqlserver数据库的配置信息
SQLSERVER_HOST = 'localhost'
SQLSERVER_DBNAME = 'pictureread'         #数据库名字，请修改
SQLSERVER_USER = 'sa'             #数据库账号，请修改
SQLSERVER_PASSWD = 'password123'         #数据库密码，请修改
SQLSERVER_PORT = 1433               #数据库端口，在dbhelper中使用
SQLSERVER_ENCODE = 'utf8'          #编码要加上，否则可能出现中文乱码问题


#Oracle数据库的配置信息
ORACLE_USER = 'caffo'             #数据库账号，请修改
ORACLE_PASSWD = 'caffo'         #数据库密码，请修改
ORACLE_DSN = 'ORCL'               #数据库服务名
ORACLE_ENCODE = 'utf8'          #编码要加上，否则可能出现中文乱码问题