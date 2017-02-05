# -*- coding: utf-8 -*-

import scrapy
from scrapy.item import Item, Field


class ResulItem(scrapy.Item):
    url = Field()
    referer = Field()
    status = Field()

    def __init__(self, url, referer, status, *args, **kwargs):
        super(ResulItem, self).__init__(*args, **kwargs)
        self['url'] = url
        self['referer'] = referer
        self['status'] = status
