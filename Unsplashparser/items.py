# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Compose

def process_photo(value):
    value = value.split()
    return value

class UnsplashparserItem(scrapy.Item):
    category= scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    photo = scrapy.Field(input_processor=MapCompose(process_photo), output_processor=TakeFirst())
    _id = scrapy.Field()

