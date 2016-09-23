
import scrapy
import json
from scrapy.selector import Selector
from BookMyShowMovies.items import BookmyshowmoviesItem


class BookmyshowSpider(scrapy.Spider):
    name = "BookMyShowSpider"
    allowed_domains = ["in.bookmyshow.com"]
    start_urls = (
        'https://in.bookmyshow.com/national-capital-region-ncr/movies',
    )

    def parse(self, response):
        movies_dict = []
        movies = response.xpath('//div[@class="wow fadeIn movie-card-container"]').extract()
        for movie in movies:
            mov = BookmyshowmoviesItem()
            mov['name'] = Selector(text=movie).xpath('//div[@class="detail"]//a[@class="__movie-name"]/text()').extract()
            mov['languages'] = Selector(text=movie).xpath('//div[@class="detail"]//div[@class="languages"]//li/text()').extract()
            mov['genre'] = Selector(text=movie).xpath('//div[@class="detail"]//div[@class="genre-list"]//a/div/text()').extract()
            # mov['rating'] = Selector(text=movie).xpath('//div[@class="stats-wrapper"]//div[@class="__percentage"]/text()').extract()
            yield mov
