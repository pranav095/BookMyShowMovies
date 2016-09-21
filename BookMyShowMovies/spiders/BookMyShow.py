# -*- coding: utf-8 -*-
import scrapy


class BookmyshowSpider(scrapy.Spider):
    name = "BookMyShow"
    allowed_domains = ["in.bookmyshow.com"]
    start_urls = (
        'http://www.in.bookmyshow.com/',
    )

    def parse(self, response):
        pass
