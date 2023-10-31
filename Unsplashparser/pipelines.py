# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline

class PhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        try:
            yield scrapy.Request(item['photo'])
        except Exception:
            print(Exception)

    def item_completed(self, results, item, info):
        if results[0][0]:
            item['photo'] = results[0][1]
        return item

class UnsplashparserPipeline:
    def process_item(self, item, spider):
        with open('dz6.csv', 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=item.keys())
            writer.writeheader()
            writer.writerow(item)

        return item