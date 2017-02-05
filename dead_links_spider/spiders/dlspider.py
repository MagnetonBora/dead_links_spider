from ..items import ResulItem
from ..settings import ALLOWED_DOMANS, START_URLS

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class DeadLinkSpider(CrawlSpider):
    name = "dead-links-spider"
    allowed_domains = ALLOWED_DOMANS
    start_urls = START_URLS
    handle_httpstatus_list = [404, 200]
    rules = (Rule(LinkExtractor(), callback='parse_entity', follow=True),)

    def parse_entity(self, response):
        if response.status == 404:
            referer = response.request.headers.get('Referer')
            return ResulItem(response.url, referer, response.status)
