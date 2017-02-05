from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ResultEntity(Item):
    url = Field()
    referer = Field()
    status = Field()

    def __init__(self, url, referer, status, *args, **kwargs):
        super(ResultEntity, self).__init__(*args, **kwargs)
        self['url'] = url
        self['referer'] = referer
        self['status'] = status


class DeadLinkSpider(CrawlSpider):
    name = "dead-links-spider"
    allowed_domains = ["yplanapp.com",]
    start_urls = ["https://yplanapp.com/bristol/nightlife"]
    handle_httpstatus_list = [404]
    rules = (Rule(LinkExtractor(), callback='parse_entity', follow=True),)

    def parse_entity(self, response):
        if response.status == 404:
            referer = response.request.headers.get('Referer')
            return ResultEntity(response.url, referer, response.status)
