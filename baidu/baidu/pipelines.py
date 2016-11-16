## -*- coding: utf-8 -*-
#
## Define your item pipelines here
##
## Don't forget to add your pipeline to the ITEM_PIPELINES setting
## See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#
from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
import hashlib
from hashlib import md5
import MySQLdb
import MySQLdb.cursors
import sys,time
from scrapy.exceptions import DropItem
from scrapy.http import Request


class MySqlStorePipeline(object):
    
    def __init__(self):
        #        远程库连接
        #        self.conn = MySQLdb.connect(user='root', passwd ='111111', db='papagif', host='192.168.2.28', charset="utf8", use_unicode=True)
        #self.conn = MySQLdb.connect(user='root', passwd ='111111', db='testgif', host='192.168.2.28', charset="utf8", use_unicode=True)
        self.conn = MySQLdb.connect(user='root', passwd ='root', db='test', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        #开始连接
        try:
            
            #以imgid/targetid 为基准获取爬取数据
            
            if item.get('imgid'):
                
                if 'customer_exceptions' in item.keys():

                    raise DropItem('some exception occurred: ('+ item['linkmd5id'] + ') ---> ' + item['customer_exceptions'] )
                
                print "---> begin db operation: " + item['linkmd5id']

                self.cursor.execute("SELECT id FROM spiderdb WHERE target_id ="+"'"+item['linkmd5id']+"'")
                
                isExist = self.cursor.fetchone()
                
                # print isExist
                
                # print "================================================================================"
                
                if isExist:
                    
                    print '------> image is already exist'
                    
                    #title, author, target_id, isSync, dimensions, category, gif_detail_url, gif_static_url, gif_thumb_url, gif_original_url, FromWebPage_url, sync_time, update_time, scrawl_time, tags
                    now = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
                    #                    now = datetime.utcnow().replace(microsecond=0).isoformat(' ')

                    #如果存在则获取数据库原有tag
                    
                    getTags = self.cursor.execute('select tags from spiderdb where target_id = "%s"' %(item['linkmd5id']))

                    temp = self.cursor.fetchall()

                    temptags = ""

                    if not temp:

                        temptags = item['tag']

                    else:

                        temptags = temp[0]

                    print '----------------------dbtemptags-------------------------'

                    print temptags;

                    print '--------------------localtemptag-------------------------'

                    print item['tag']

                    localtemptag = str(item['tag']).split(',')

                    print localtemptag

                    dbtemptags = str(temptags[0]).split(',')

                    print dbtemptags

                    uploadtags = list(set(localtemptag).union(set(dbtemptags)))

                    print '======update tags======='

                    temptags = ""

                    print uploadtags

                    for strings in uploadtags:
                        
                        print '<-----strings:----->' + strings

                        tempstr = strings + ','

                        temptags += tempstr

                    print temptags

                    temptags = temptags[:-1]

                    item['updateTime'] = now
                    
                    #isSync 执行一次update 就会自动置为false scrawl_time 与 updateTime 初始值相同 当 update执行后 updatetime更新
                    # self.cursor.execute("update spiderdb set title = %s, author = %s, is_sync = %s, dimensions = %s, size = %s, frame = %s, category = %s, gif_detail_url = %s, gif_static_url = %s, gif_thumb_url = %s, gif_original_url = %s, source_web_url = %s, update_time = %s, tags = %s WHERE target_id = %s",(item['title'],item['author'],"0",item['imgsize'], item['filesize'] , item['frame'] ,item['category'],item['middleURL'],item['hoverURL'],item['thumbURL'],item['objURL'],item['fromURL'],now,item['tag'],item['linkmd5id']))
                    self.cursor.execute("update spiderdb set  is_sync = %s,update_time = %s, tags = %s WHERE target_id = %s",( "0",now,temptags,item['linkmd5id']))
                    
                    self.conn.commit()
                    
                    print '------> database has been updated'

                    # self.cursor.close()

                    # self.conn.close()
            
                else:
                    #执行insert 指令 isSync 默认为 false
                    # self.cursor.execute("INSERT INTO spiderdb (title, author, target_id, dimensions, size, frame ,category, gif_detail_url, gif_static_url, gif_thumb_url, gif_original_url, source_web_url, is_sync, update_time, scrawl_time, tags) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s ,%s)",(item['title'],item['author'],item['linkmd5id'],item['imgsize'], item['filesize'] , item['frame'] ,item['category'],item['middleURL'],item['hoverURL'],item['thumbURL'],item['objURL'],item['fromURL'],"0",item['updateTime'],item['scrawl_time'],item['tag']))
                    self.cursor.execute("INSERT INTO spiderdb (title, author, target_id, dimensions, size, frame ,category, source_web_url, source_thumb_url, source_original_url, is_image_download , is_sync, update_time, scrawl_time, tags) VALUES (%s, %s, %s, %s, %s , %s, %s, %s, %s, %s , %s, %s, %s, %s, %s)",(item['title'],item['author'],item['linkmd5id'],item['imgsize'], item['filesize'] , item['frame'] ,item['category'], item['fromURL'],item['source_thumb_url'], item['source_original_url'], "0" , "0",item['updateTime'],item['scrawl_time'],item['tag']))
                    
                    self.conn.commit()
                    print '------> image has been inserted'

                
                print '\n-----------------------------------------------------------------------------------------------------------------------------\n'   

        except MySQLdb.Error, e:
        
            # print "Error %d: %s" % (e.args[0], e.args)
            print 'Error---->'

            print e.args

            # self.cursor.close()

            # self.conn.close()

            print 'database has been closed!'
        
        return item
























