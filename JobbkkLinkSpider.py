import scrapy
from ..links import SeniorresearchLink



class QuoteSpider(scrapy.Spider):

    name = 'jobbkkLinkSpider'

    with open ('realOgLinks.csv') as file:
        start_urls = [line.strip() for line in file]

    custom_settings = {
        'FEEDS': {'links.csv': {'format': 'csv', 'overwrite': True }}
        }

    def parse(self, response):

        links = SeniorresearchLink()

        linkall = response.css('a.positon-work::attr(href)').extract()



        links['linkall'] = linkall

        yield links

