import sys

# sys.path.append('/usr/src/utils/news_parser/scrapy_parser/spiders')
sys.path.append('D:\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\spiders')
sys.path.append('D:\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\utils')
import scrapy
from main_spider import MainSpider

class PgdSpider(MainSpider):

    name = "pgd"
    start_urls = ['https://www.playground.ru/news/industry']

    def __init__(self):
        self.link_path = "//div[@class='post-title']/a/@href"
        self.title_path = "//h1[@class = 'post-title']/text()"
        self.text_path = "//div[@class ='article-content js-post-item-content']/descendant::text()"
        self.date_time_path = "//div[@class='post-metadata']/div/time/@datetime"
        self.image_path = "//figure/a/@href | //figure/img/@src | //div[@class='ytp-cued-thumbnail-overlay-image']/@style"
        self.site_base_link = "https://www.playground.ru"
        self.site_name = 'pgd'

#to run: scrapy runspider pgd_spider.py