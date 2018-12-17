# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class WubaPipeline(object):
    def __init__(self):
        self.f = open('wubasj.csv','a',encoding='utf-8')
        self.mywrite = csv.writer(self.f,delimiter=' ')
        self.mywrite.writerow(['bendi', 'gongsi', 'mingcheng', 'miaoshu', 'lianjie'])
    def process_item(self, item, spider):
        bendi = item['bendi']
        gongsi = item['gongsi']
        mingcheng = item['mingcheng']
        miaoshu = item['miaoshu']
        lianjie = item['lianjie']


        self.mywrite.writerow([bendi, gongsi, mingcheng, miaoshu, lianjie])
        return item
    def cloxe_spider(self,spider):
        self.f.close()
