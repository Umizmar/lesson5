import scrapy
from scrapy.http import HtmlResponse
from Unsplashparser.items import UnsplashparserItem
from scrapy.loader import ItemLoader

class UnsplashSpider(scrapy.Spider):
    name = "Unsplash"
    allowed_domains = ["unsplash.com"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.category = kwargs.get('query')
        self.start_urls = [f"https://unsplash.com/s/photos/{self.category}"]

    def parse(self, response:HtmlResponse):
        links = response.xpath("//a[@itemprop='contentUrl']")
        for link in links:
            yield response.follow(link, callback=self.parse_phot)

    def parse_phot(self, response:HtmlResponse):
        loader = ItemLoader(item=UnsplashparserItem(), response=response)
        loader.add_xpath('name', '//h1/text()')
        loader.add_value('category', self.category)
        loader.add_value('url', response.url)
        loader.add_xpath('photo', "//div[@class='MorZF']/img/@srcset")
        yield loader.load_item()

