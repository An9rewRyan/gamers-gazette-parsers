import sys
# sys.path.append('/usr/src/utils/news_parser/scrapy_parser/spiders')
sys.path.append('D:\\game_news_parser\\main_parser\\spiders')
import scrapy
from main_spider import MainSpider
import json

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
        begin_of_json_index = date_time.find('>')
        end_of_json_index = date_time.find('</')
        date_time = date_time[begin_of_json_index+1:end_of_json_index]
        date_time_json = json.loads(date_time)
        date_time = date_time_json["datePublished"]
        return date_time

# to run: scrapy runspider sg_spider.py
