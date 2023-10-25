# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class BookparsePipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_b = client.books

    def process_item(self, item, spider):
        if item['author_link']:
            item['author_link'] = 'www.labirint.ru'+ item['author_link']

        collections = self.mongo_b[spider.name]
        collections.insert_one(item)

        return item
