import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'Quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://http://quotes.toscrape.com/']

    def parse(self, response):
        pass
