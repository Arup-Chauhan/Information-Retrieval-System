import os
from pathlib import Path
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider

class SneakerCrawlerSpider(CrawlSpider):
    name = "sneaker_crawler"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Sneakers"]
    custom_settings = {'DEPTH_LIMIT': 3 , 'CLOSESPIDER_PAGECOUNT': 250 }

    link_extractor = LinkExtractor(restrict_css='#mw-content-text > div.mw-content-ltr.mw-parser-output > p')
    rules = (
        Rule(link_extractor, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        content_area = response.css("div.mw-content-ltr")
        current_page = response.url.split("/")[-1]
        
        document_dir = "C:\\Users\\arupd\\Documents\\Academics\\CS 429\\Project\\Final Iteration\\CS429-IR-Project-Deployment\\Sneaker Space Web Crawler\\ScrappedDocuments"
        document_name = f"sneaker_space-{current_page}.html"
        document_path = Path(os.path.join(document_dir, document_name))
        document_path.write_bytes(response.body)
        
        title = content_area.css("span.mw-page-title-main::text").get()
        details = "".join(content_area.css("p::text").getall()).replace("\n", " ")
        
        yield {
            "Sneaker Title": title.strip() if title else 'No Title',
            "Sneaker Details": details if details.strip() else 'No Details',
            "Visit": response.url
        }
        
        for link in content_area.css("div.mw-content-ltr p a::attr(href)").extract():
            if link.startswith("/wiki/") and ':' not in link:
                next_page_url = response.urljoin(link)
                yield scrapy.Request(next_page_url, callback=self.parse_item)