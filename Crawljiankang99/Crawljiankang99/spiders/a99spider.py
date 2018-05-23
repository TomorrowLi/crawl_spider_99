# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import jiankangItemLoader , Crawljiankang99Item


class A99spiderSpider(CrawlSpider):
    name = '99spider'
    allowed_domains = ['www.99.com.cn',
                       'nv.99.com.cn',
                       'ye.99.com.cn',
                       'zyk.99.com.cn',
                       'jf.99.com.cn',
                       'fk.99.com.cn',
                       'zx.99.com.cn',
                       'bj.99.com.cn',
                       'nan.99.com.cn',
                       'nan.99.com.cn',
                       'jz.99.com.cn',
                       'gh.99.com.cn',
                       'news.99.com.cn']
    deny_domains=[]
    start_urls = ['http://www.99.com.cn/']
    rules = (
        #Rule(LinkExtractor(allow=r"http://.*.99.com.cn/"),follow=True),
        Rule(LinkExtractor(allow=r'.*/\d+.htm',deny=(r'/jijiu/jjsp/\d+.htm',r'/jzzn/.*/\d+.htm',r'/ssbd/jfsp/\d+.htm'
                                                     ,r'/zhongyiyangshengshipin/.*/.html',)), callback='parse_item', follow=True,),
    )

    def parse_item(self, response):
        image_url=response.css('.detail_con img::attr(src)').extract_first()
        item_loader=jiankangItemLoader(item=Crawljiankang99Item(),response=response)
        item_loader.add_css('title','.title_box h1::text')
        item_loader.add_value('url',response.url)
        item_loader.add_css('content','.detail_con')
        item_loader.add_value('image_url',[image_url])


        jiankang=item_loader.load_item()


        return jiankang
