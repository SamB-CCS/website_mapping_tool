# MAP ALL URLS
from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
import json


class MyCrawler(Spider):
    name = 'mycrawler'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']  # replace with your website's URL
    custom_settings = {
        'FEEDS': {
            'output.json': {
                'format': 'json',
            },
        },
    }

    def __init__(self, *args, **kwargs):
        super(MyCrawler, self).__init__(*args, **kwargs)
        self.visited_urls = set()

    def parse(self, response):
        le = LinkExtractor()
        for link in le.extract_links(response):
            # comment out next two lines if you don't want to remove duplicates and indent yield lines
            if link.url not in self.visited_urls:
                self.visited_urls.add(link.url)
                yield {
                    'source_url': response.url,
                    'target_url': link.url
                }
                yield Request(link.url, callback=self.parse)


# to execute run - scrapy crawl mycrawler -o output.json




