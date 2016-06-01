# -*- coding: utf-8 -*-
import scrapy

# crawl spider is better

from scrapy.contrib.spiders import CrawlSpider


class PicSpider(CrawlSpider):
    name = "pic"
    allowed_domains = ["www.reddit.com"]
    start_urls = (
        'http://www.reddit.com/r/pics/',
    )

    def parse(self, response):
        pass
