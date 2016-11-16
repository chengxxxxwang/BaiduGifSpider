#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
##filename = ConnectToTestDB.py
##author:chenxingwang
##
#

import MySQLdb
import sys
import time
timer = time.ctime()
year = timer.split(" ")[4]
reload(sys)
sys.setdefaultencoding("utf-8")


# testDB
def conn_dbTest():
    conn = MySQLdb.connect(
                           host='192.168.2.28',
                           port=3306,
                           user='root',
                           passwd='111111',
                           db="papagif",
                           charset="utf8"
                           )
    return conn


# Mylocalhost数据库
def conn_dbMyLoacl():
    conn = MySQLdb.connect(
                           host='localhost',
                           port=3306,
                           user='root',
                           passwd='root',
                           db="test",
                           charset="utf8"
                           )
    return conn

#获取本地表单数据
def data(table):
    conn = conn_dbMyLoacl()
    cur = conn.cursor()
    sql = "select * from " + "".join(table)
    cur.execute(sql)
    datas = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    return datas


#获取所有isSync为0的图片

def getLocalDB_status(table):
    conn = conn_dbMyLoacl
    cur = conn.cursor()
    sql = "select * from " + "".join(table) + " where isSync = 0"
    cur.execute(sql)
    datas = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    return datas

#将本地表单导入到远程表重置isSync
def transport_data_to_remote():
    conn = ConnectToTestDB
    cur = conn.cursor()
    sql = "update spiderdb set isSync = 1 where target_id = %s",target_id


#将gif表单中tag分离出传入tag和tag_gif表单
def update_gif_tag(tag):
    #查 tag
    conn = ConnectToTestDB
    cur = conn.cursor()
    tag = data("tag")
    for i in range(len(tag)):
        sql = "select *id from tag where tag =" +tag[i]
        cur.execute(sql)



#更新本地表单继续上传


