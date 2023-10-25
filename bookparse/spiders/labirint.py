import scrapy
from scrapy.http import HtmlResponse
from bookparse.items import BookparseItem
class LabirintSpider(scrapy.Spider):
    name = "labirint"
    allowed_domains = ["www.labirint.ru"]
    start_urls = ["https://www.labirint.ru/genres/1850/"]

    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//a[@class='pagination-next__text']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//div[@data-title='Все в жанре «Книги для детей»']//a[@class='product-title-link']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.book_parse)


    def book_parse(self, responce:HtmlResponse):
        name = responce.xpath("//h1/text()").get()
        price = responce.xpath("//span[@class='buying-pricenew-val-number']/text()").get()
        author_link = responce.xpath("//div[@class='authors']//@href").get()
        yield BookparseItem(name=name, price=price, author_link=author_link)


