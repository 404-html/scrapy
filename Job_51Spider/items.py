# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Job51Item(scrapy.Item):
    position = scrapy.Field()
    positionType = scrapy.Field()
    salary = scrapy.Field()
    city = scrapy.Field()
    firm = scrapy.Field()
    business = scrapy.Field()
    firmSize = scrapy.Field()
    welfare = scrapy.Field()
    firmType = scrapy.Field()
    education = scrapy.Field()
    experience = scrapy.Field()
    positionDetail = scrapy.Field()
    time = scrapy.Field()
    numHire = scrapy.Field()
    web = scrapy.Field()