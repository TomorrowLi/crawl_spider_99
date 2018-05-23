# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors
from scrapy.pipelines.images import ImagesPipeline
class jiankangImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if 'image_url' in item:
            for ok,value in results:
                image_file_path=value['path']
            item['image_url_path']=image_file_path
        return item
class Crawljiankang99Pipeline(object):
    def process_item(self, item, spider):
        return item
class MysqlTwistePipline(object):
    def __init__(self,dbpool):
        self.dbpool=dbpool
    @classmethod
    def from_settings(cls,settings):
        dbparms=dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DB'] ,
            user=settings['MYSQL_USER'] ,
            passwd=settings['MYSQL_PASSWORD'] ,
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool=adbapi.ConnectionPool('MySQLdb',**dbparms)
        return cls(dbpool)

    def process_item(self , item , spider):
        #使用twisted将musql变成异步操作
        query=self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.hand_erro)
    def hand_erro(self,failure):
        print(failure)
    def do_insert(self,cursor,item):
        url = item['url']
        image_urls = item['image_url']
        image_url = image_urls[0]
        content = item['content']
        title = item['title']
        image_url_path=item['image_url_path']
        cursor.execute(
            'insert into jiankang(url,title,image_url,image_url_path,content) values(%s,%s,%s,%s,%s)' ,
            (url,title,image_url,image_url_path,content))
