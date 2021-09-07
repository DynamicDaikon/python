import scrapy
class TutorialItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
