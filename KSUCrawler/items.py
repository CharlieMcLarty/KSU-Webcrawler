import scrapy


class KSUItem(scrapy.Item):
    pageid = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()
    email = scrapy.Field()
