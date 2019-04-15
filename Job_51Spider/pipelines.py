# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Job51SpiderPipeline(object):
    def process_item(self, item, spider):
        with open('Job51.txt', 'a', encoding='utf-8') as fp:
            fp.write(
                item['position'] + '\t' +
                item['positionType'] + '\t' +
                item['salary'] + '\t' +
                item['city'] + '\t' +
                item['firm'] + '\t' +
                item['business'] + '\t' +
                item['firmSize'] + '\t' +
                item['welfare'] + '\t' +
                item['firmType'] + '\t' +
                item['education'] + '\t' +
                item['experience'] + '\t' +
                item['positionDetail'] + '\t' +
                item['time'] + '\t' +
                item['numHire'] + '\t' +
                item['web'] + '\n'
            )
