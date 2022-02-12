import sys
# sys.path.append('/usr/src/utils/news_parser/scrapy_parser/spiders')
sys.path.append('D:\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\spiders')
sys.path.append('D:\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\utils')

import scrapy
from main_spider import MainSpider
from get_json_from_script_tag import get_info_from_json

class SgSpider(MainSpider):

    name = "sg_site"
    start_urls = ['https://stopgame.ru/news/industry']

    def __init__(self):

        self.link_path = "//a[@class='article-image']/@href"
        self.title_path = "//h1[@class ='article-title']/text()"
        self.text_path = "//section[@class='article']/descendant::text()[ancestor::p or ancestor::ul]"
        self.date_time_path = "//script[@type='application/ld+json']"
        self.image_path = "//section[@class='article']/descendant::img/@src | //div[@class='iframe_h']/data-iframe/@data-preroll-thumb"
        self.site_base_link = "https://stopgame.ru"
        self.site_name = 'sg'
    
    def format_image(self, response):
        image = super(SgSpider, self).format_image(response)
        if ',' in image:
            image = image.split(',')[0]
        return image

    #данные берутся из скрытого js файла
    def format_date_time(self, response):
        date_time = super(SgSpider, self).format_date_time(response)
        date_time = get_info_from_json(date_time, "datePublished")
        return date_time

# to run: scrapy runspider sg_spider.py
