import scrapy
from tutorial.items import TutorialItem
class quotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = TutorialItem()
            item['author'] = quote.css('small.author::text').extract_first()
            item['text'] = quote.css('span.text::text').extract_first()
            item['tags'] = quote.css('div.tags a.tag::text').extract()
            yield item

