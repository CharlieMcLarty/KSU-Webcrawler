from hashlib import md5
from KSUCrawler.items import KSUItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class KSUSpider(CrawlSpider):
    name = "ksu"
    allowed_domains = ["kennesaw.edu"]
    start_urls = [
        "https://www.kennesaw.edu",
        "https://www.kennesaw.edu/parking/",
        "https://www.kennesaw.edu/dining/"
    ]

    rules = (
        Rule(
            LinkExtractor(
                allow_domains=['kennesaw.edu'],
                canonicalize=True,
                unique=True,
            ),
            callback='parse_item',
            follow=True
        ),
    )

    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 1000,
        'DEPTH_PRIORITY': 1,
        'SCHEDULER_DISK_QUEUE': 'scrapy.squeues.PickleFifoDiskQueue',
        'SCHEDULER_MEMORY_QUEUE': 'scrapy.squeues.FifoMemoryQueue',
    }

    def parse_item(self, response):
        self.logger.info("Parsing: %s", response.url)
        item = KSUItem()
        item['url'] = response.url
        item['pageid'] = md5(item['url'].encode('utf-8')).hexdigest()
        item['body'] = response.css("body").get()
        item['title'] = response.css("title::text").get()
        item['email'] = response.css("body").re(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
        yield item
