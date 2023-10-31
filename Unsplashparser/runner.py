import random

from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from Unsplashparser.spiders.Unsplash import UnsplashSpider


if __name__ == '__main__':
    install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
    configure_logging()
    process = CrawlerProcess(get_project_settings())
    process.crawl(UnsplashSpider, query=random.choice(['food', 'chef', 'relax', 'beauty', 'sports']))
    process.start()