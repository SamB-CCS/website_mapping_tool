# SITEMAP GENERATOR
import scrapy
class SitemapSpider(scrapy.Spider):
    name = 'sitemap_spider'
    start_urls = ['https://books.toscrape.com/']  # replace with your website's URL

    def parse(self, response):
        for url in response.xpath('//a/@href').extract():
            yield {'url': response.urljoin(url)}

# to execute run - scrapy crawl sitemap_spider -o sitemap1.xml