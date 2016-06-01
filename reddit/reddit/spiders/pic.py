# -*- coding: utf-8 -*-
import scrapy

# crawl spider is better

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PicSpider(CrawlSpider):
    name = "pic"
    allowed_domains = ["www.reddit.com"]
    start_urls = (
        'http://www.reddit.com/r/pics/',
    )
    rules = [
        Rule(LinkExtractor(allow=['.*']))
    ]

    def parse(self, response):
        pass
