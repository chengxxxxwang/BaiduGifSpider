#!/usr/bin/env python
#coding=utf-8
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request, FormRequest
from baidu.items import BaiduItem
from datetime import datetime
from time import sleep
import urllib,urllib2
from PIL import Image,ImageSequence
import os,sys,time,shutil
import sys
import string
import json
import hashlib
import imageio

reload(sys)
sys.setdefaultencoding('utf-8')


class Gifcrawl(CrawlSpider):

    name='ajaxBaidu'

    start_urls=[
                "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E6%9D%8E%E6%98%93%E5%B3%B0gif&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E6%9D%8E%E6%98%93%E5%B3%B0gif&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=30&rn=30&gsm=5a&1469159068915="
                ]

    allowed_domains = ["image.baidu.com"]

    headers ={

        "Accept":"text/plain, */*; q=0.01",
        "X-DevTools-Emulate-Network-Conditions-Client-Id":"C831DB41-AF82-42C9-BB32-89713946FA7A",
        "X-Requested-With":"XMLHttpRequest",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Referer":"http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C0%EE%D2%D7%B7%E5gif&fr=ala&ala=2",
        "Accept-Encoding":"gzip, deflate, sdch",
        "Accept-Language":"zh-CN,zh;q=0.8"
    }
    cookies = {
        'BDRCVFR[-pGxjrCMryR]':r'mk3SLVN4HKm',
        'BAIDUID':r'023C332D7914D339266BDF350CAC18AC:FG=1',
        'BIDUPSID':'023C332D7914D339266BDF350CAC18AC',
        'PSTM':r'1466229312',
        'pgv_pvi':r'4231836672',
        'H_PS_PSSID':r'19684_1454_20415_15468_11753',
        'BDRCVFR[dG2JNJb_ajR]':r'mk3SLVN4HKm',
        'BDqhfp':r'%25CD%25F5%25C4%25E1%25C2%25EAgif%26%26NaN-1undefined%26%264482%26%266',
        'BDIMGISLOGIN':r'0',
        'BAIDUID':r'023C332D7914D339266BDF350CAC18AC:FG=1',
        'BIDUPSID':r'023C332D7914D339266BDF350CAC18AC',
        'PSTM':r'1466229312',
        'pgv_pvi':r'4231836672',
        'BDRCVFR[dG2JNJb_ajR]':r'mk3SLVN4HKm',
        'BDRCVFR[-pGxjrCMryR]':r'mk3SLVN4HKm',
        'pgv_si':r's373898240',
        'H_PS_PSSID':r'19684_1454_20415_15468_11753'
    }

    def start_requests(self):

        print "begin parse input file."
        # base = '/Users/Apple/Desktop/'

        f = open('/spiders/keywords_bak.txt ', 'r')

        line = f.readline()

        tag        = ""
        category   = ""
        dict       = {}
        keywords   = []
        categories = []
        tags       = []
        url_keys   = []
        myURLs     = []
        dicts      = []
        pages      = []

        while line:
            print line,                 # 后面跟 ',' 将忽略换行符
            print line.split('|')
            tmpData = line.split('|')
            check_pages = len(tmpData)
            if check_pages <= 3:
                page = 2 #defaut page is 2
            elif check_pages = 4:
                page = int(tmpData[3])
            else:
                pass
                print 'len of list > 4'
            keyword = line.split('|')[0]
            category = line.split('|')[1]
            tag = line.split('|')[2]
            categories.append(category)
            tags.append(tag)
            keywords.append(keyword)
            pages.append(page)
            #预留字典传参时使用
            dict = {"tag":tag,"category":category,"keyword":keyword}
            dicts.append(dict)

            line = f.readline()
            # print '----img----'
                #读取 keyword

        f.close()

        print pages

        print "begin build request urls"

        for i in xrange(0,len(dicts)):
            print keywords[i]
            url = keywords[i]
            #输出 utf-8 url 编码方便之后使用
            print urllib.quote(url)
            url_key = urllib.quote(url)
            url_keys.append(url_key)
            page = pages[i]
            #查2页数据 每页 30条 数据
            for i in xrange(0,page):

                pn = 30 * i

                str_pn = str(pn)

                auto_url = "http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=" + url_key +"gif&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=" + url_key + "gif&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn="+str_pn+"&rn=30&gsm=5a&1469159068915="
                myURLs.append(auto_url)

#        print myURLs

#        print tags



        len_url = len(myURLs)

        for i in xrange(0,len_url):

            url      = myURLs[i]
            count    = pages[i]
            j = i // count #除数需和查询页数 xrange 中的数字一致 否则会有数组越界问题

            print j

            tag      = tags[j]

            category = categories[j]

            yield Request(url, headers ={
                          "Accept":"text/plain, */*; q=0.01",
                          "X-DevTools-Emulate-Network-Conditions-Client-Id":"C831DB41-AF82-42C9-BB32-89713946FA7A",
                          "X-Requested-With":"XMLHttpRequest",
                          "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
                          "Referer":"http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gbk&word=%C0%EE%D2%D7%B7%E5gif&fr=ala&ala=2",
                          "Accept-Encoding":"gzip, deflate, sdch",
                          "Accept-Language":"zh-CN,zh;q=0.8"
                          },cookies = {
                          'BDRCVFR[-pGxjrCMryR]':r'mk3SLVN4HKm',
                          'BAIDUID':r'023C332D7914D339266BDF350CAC18AC:FG=1',
                          'BIDUPSID':'023C332D7914D339266BDF350CAC18AC',
                          'PSTM':r'1466229312',
                          'pgv_pvi':r'4231836672',
                          'H_PS_PSSID':r'19684_1454_20415_15468_11753',
                          'BDRCVFR[dG2JNJb_ajR]':r'mk3SLVN4HKm',
                          'BDqhfp':r'%25CD%25F5%25C4%25E1%25C2%25EAgif%26%26NaN-1undefined%26%264482%26%266',
                          'BDIMGISLOGIN':r'0',
                          'BAIDUID':r'023C332D7914D339266BDF350CAC18AC:FG=1',
                          'BIDUPSID':r'023C332D7914D339266BDF350CAC18AC',
                          'PSTM':r'1466229312',
                          'pgv_pvi':r'4231836672',
                          'BDRCVFR[dG2JNJb_ajR]':r'mk3SLVN4HKm',
                          'BDRCVFR[-pGxjrCMryR]':r'mk3SLVN4HKm',
                          'pgv_si':r's373898240',
                          'H_PS_PSSID':r'19684_1454_20415_15468_11753'
                          },callback = lambda response,typeid=tag,test=category:self.parse(response,typeid,test))


    def parse(self, response,typeid,category):

        print "---> begin execute parse method"

        item = BaiduItem()
        items = []
#        print response.body

        print "---> tags: " + typeid

        data = response.body
        # print data

        print"---> category: " + category

        s = json.loads(data)

#        print s

        MyData = s["data"]

#        print "Data++++++++"

#        print data



        num = len(MyData)

        for i in xrange(0,num - 1):

#            print MyData[i]

            print '\n--------------------------------------------------------------------------%d---------------------------------------------------\n' %(i)


            print '---> now is : ' + str(time.strftime('%Y-%m-%d %H:%M %S',time.localtime(time.time())))

            # print MyData[i]["hoverURL"]

            width = MyData[i]["width"]
            height = MyData[i]["height"]

            size = str(width)+"*"+str(height)

            print '---> title: ' + MyData[i]["fromPageTitleEnc"]


            #测试下载使用gif地址
            # image = str(MyData[i]["middleURL"])
            # print "image------->" + image

            simid = MyData[i]["os"]
            Hash = simid.split(",")[0]

#            now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
            now = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

            item['imgsize']     = size
            item['imgid']       = Hash
            item['category']    = category
            item['tag']         = typeid
            item['updateTime']  = now
            item['scrawl_time'] = now
            item['title']       = MyData[i]["fromPageTitleEnc"]
            item['fromURLHost'] = MyData[i]["fromURLHost"]
            item['author']      = MyData[i]["fromURLHost"]

            ObjURL = MyData[i]["objURL"]

            fromURL = MyData[i]["fromURL"]

            e = {"w": "a","k": "b","v": "c","1": "d","j": "e","u": "f","2": "g","i": "h","t": "i","3": "j","h": "k","s": "l","4":"m","g":"n","5": "o","r": "p","q": "q","6": "r","f": "s","p": "t","7": "u","e": "v","o": "w","8": "1","d": "2","n": "3","9": "4","c": "5","m": "6","0": "7","b": "8","l": "9","a": "0","_z2C$q": ":","_z&e3B": ".","AzdH3F": "/"}

            #破译obj编码 使用字符替换 没有使用正则(正则学的太烂) TODO:正则

            print ObjURL

            ekeys = e.keys()

#            print ekeys

            strLength = len(ekeys)

            URL_O = ObjURL
            URL_O = URL_O.replace("_z2C$q",":")
            URL_O = URL_O.replace("_z&e3B",".")
            URL_O = URL_O.replace("AzdH3F","/")
            URLLength = len(URL_O)
            print URL_O


            URL_F = fromURL
            URL_F = URL_F.replace("_z2C$q",":")
            URL_F = URL_F.replace("_z&e3B",".")
            URL_F = URL_F.replace("AzdH3F","/")
            URL_FLength = len(URL_F)
            s_f = ""

            #解析fromURL TODO
            for j in xrange(0,URL_FLength):
                URLKey = URL_F[j]
                url = ord(URLKey)
                if (url >= ord('a') and url <= ord('w')) or (url >= ord('0') and url <= ord('9')):
                    str_url = e[str(URLKey)]
                    s_f = s_f + str_url
                else:
                    s_f = s_f + URLKey
            print s_f

            s = ""
            for j in xrange(0,URLLength):
                URLKey = URL_O[j]
                url = ord(URLKey)
                if (url >= ord('a') and url <= ord('w')) or (url >= ord('0') and url <= ord('9')):
                    str_url = e[str(URLKey)]
                    s = s + str_url
                else:
                    s = s + URLKey

            hash_url = hashlib.md5(s).hexdigest()[8:-8]


            item['linkmd5id'] = hash_url

            print "---> hash_url: "+ hash_url
            print "---> url_orgin: " + s

            #图片下载本地地址
            # path = "/Users/chenxingwang/Desktop/"+ category +"/"+hash_url[:2]+"/"+hash_url
            uploadUrl = "/"+ category +"/"+hash_url[:2]+"/"+hash_url
            path = "../output/gif" + uploadUrl

            print "---> folder for saving image: " + path

            # isExists=os.path.exists(path)

            # if not isExists:
            #     os.makedirs(path)

            origin_filename = "origin.gif"
            static_filename = "static.jpg"
            thumb_filename = "thumb.gif"
            detail_filename = "detail.gif"

            url_orgin         = s
            url_thumb         = MyData[i]["thumbURL"]+".gif"
            url_hover         = MyData[i]["hoverURL"]
            url_middle        = MyData[i]["middleURL"]+".gif"
            item['fromURL']   = s_f
            item['objURL']    = uploadUrl + "/" + origin_filename
            item['hoverURL']  = uploadUrl + "/" + static_filename
            item['thumbURL']  = uploadUrl + "/" + thumb_filename
            item['middleURL'] = uploadUrl + "/" + detail_filename
            item['filesize'] = 0
            item['frame'] = 0
            item['source_thumb_url'] = url_thumb
            item['source_original_url'] = s
            sleep(1)
            yield item
            # items.append(item)


            # STEP 1. 下载缩略图
            # print "---> STEP 1. begin download thumb image: " + url_thumb
            # req = urllib2.Request(url_thumb, headers={
            #             "Upgrade-Insecure-Requests":"1",
            #             "X-DevTools-Emulate-Network-Conditions-Client-Id":"7A55439C-E6CF-420D-B294-7635B17E648B",
            #             "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            #             "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            #             "Accept-Encoding":"gzip, deflate, sdch",
            #             "Accept-Language":"zh-CN,zh;q=0.8"})

            # try:
            #     # print "thumb image to download ----------->" + url_thumb

            #     img_path= path + "/" + thumb_filename
            #     imgData = urllib2.urlopen(req).read()
            #     f = file(img_path,"wb")
            #     f.write(imgData)
            #     f.close()

            #     # generate static.jpg
            #     Image.open(img_path).convert('RGB').save(path + "/" + static_filename)

            #     print('------> thumb image downloaded. saved to ' + img_path)

            # except IOError as err:
            #     print("------> IO error:{0}".format(err))
            # except:
            #     print '------> download thumb image occured some error'
            #     print("------> Unexpected error:",sys.exc_info())



            # file_name = path + "/" + origin_filename

            # # STEP 2. 下载原图
            # print "---> STEP 2. begin download origin image: " + url_orgin
            # try:
            #     # 2 / 0
            #     urllib.urlretrieve(url_orgin, '%s' %(file_name))
            #     print('------> origin image downloaded. saved to ' + file_name)
            # except IOError as err:
            #     print("------> IO error:{0}".format(err))
            # except:
            #     print("------> Unexpected error:",sys.exc_info())
            #     print '------> download origin image occurred some error, skip this item. !!!!!!!!!!!!!!!!!!!'
            #     item['customer_exceptions'] = 'download origin image occurred some error'
            #     yield item



            # STEP 3. 生成详情图：detail.gif
            # print "---> STEP 3. begin generate detail image"
            # try:
            #     # extract fileinfo of origin.gif
            #     im = Image.open(file_name)
            #     # in KB
            #     origin_size =  os.stat(file_name).st_size / 1024
            #     item['filesize'] = str(origin_size)

            #     origin_frame_count = 1
            #     try:
            #         while 1:
            #             im.seek(im.tell()+1)
            #             origin_frame_count = origin_frame_count + 1
            #     except EOFError:
            #         pass # end of sequence

            #     item['frame'] = str(origin_frame_count)

            #     print "------> origin image info : size-" + str(origin_size) + "KB, frames-" + str(origin_frame_count)

            #     # generate detail.gif
            #     origin_size_threshold = 1.5
            #     if origin_size > origin_size_threshold * 1024 :
            #         print "------> origin image is bigger than " + str(origin_size_threshold) + "M"
            #         im = Image.open(file_name)
            #         tmp_path = path + "/temp/"
            #         if not os.path.exists(tmp_path):
            #             os.makedirs(tmp_path)

            #         print '------> origin file info: ' + str(im.info)

            #         if 'duration' in im.info.keys():
            #             origin_duration = im.info['duration'] / 1000.00
            #         else:
            #             origin_duration = 0


            #         temp_filenames = []
            #         # index = 1

            #         reader = imageio.get_reader(file_name)
            #         for i, tmp_im in enumerate(reader):
            #             imageio.imwrite("%sframe%d.png" % (tmp_path, i),tmp_im)
            #             temp_filenames.append("%sframe%d.png" % (tmp_path, i))

            #         # for frame in ImageSequence.Iterator(im):
            #         #     frame.save("%sframe%d.png" % (tmp_path, index))
            #         #     temp_filenames.append("%sframe%d.png" % (tmp_path, index))
            #         #     index += 1

            #         # print temp_filenames

            #         with imageio.get_writer(path + "/" + detail_filename, mode='I', duration=origin_duration ) as writer:
            #             for temp_filename in temp_filenames:
            #                 tmp_im = Image.open(temp_filename)
            #                 tmp_im.thumbnail((230,230))
            #                 tmp_im.save(temp_filename)
            #                 image = imageio.imread(temp_filename)
            #                 writer.append_data(image)

            #         shutil.rmtree(tmp_path)
            #         print '------> end: generate detail.gif'
            #     else:
            #         print "------> copy origin.gif as detail.gif"
            #         shutil.copyfile(file_name, path + "/" + detail_filename)

            #     # a = 2 / 0

            # except IOError as err:
            #     print("------> IO error:{0}".format(err))
            # except:
            #     print("------> Unexpected error:",sys.exc_info())
            #     print '------> generate detail.gif  occured some error'


            # print "---> finished data parse : " + hash_url

            # yield item

            # sleep(1)
