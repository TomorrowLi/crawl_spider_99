# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst , MapCompose
from w3lib.html import remove_tags

class jiankangItemLoader(ItemLoader):
    #自定义item
    default_output_processor = TakeFirst()
def return_value(value):
    return value
class Crawljiankang99Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url=scrapy.Field()
    title=scrapy.Field()
    image_url=scrapy.Field(
        output_processor=MapCompose(return_value)
    )
    image_url_path=scrapy.Field()
    content=scrapy.Field(
        input_processor=MapCompose(remove_tags)
    )

