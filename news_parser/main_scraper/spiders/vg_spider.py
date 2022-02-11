import sys
# sys.path.append('/usr/src/utils/news_parser/scrapy_parser/spiders')
sys.path.append('D:\\game_news_parser\\main_parser\\spiders')
import scrapy
from main_spider import MainSpider

class VgSpider(MainSpider):

    name = "vg_site"
    start_urls = ['https://vgtimes.ru/tags/%D0%98%D0%B3%D1%80%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8/']

    def __init__(self):

        self.link_path = "//div[@class = 'item-name type0']/a[1]/@href"
        self.title_path = "//h1[@class ='news_item_title']/text()"
        self.subtitle = ''
        self.text_path = "//p/text() | //h2/text() | //div[@class = 'v12']/ul[not(@class)]/li/text() | //div[@class = 'v12']/ul[not(@class)]/li/a/text() | //p/a[@class='l_ks' or @class='gatx']/text()"
        self.date_time_path = "//div[@class='news_item_date']/meta[1]/@content"
        self.image_path = "//div[@class='news_item_image_img']/img/@data-src"
        self.site_base_link = "https://vgtimes.ru"
        self.site_name = 'vg'

#to run: scrapy runspider vg_spider.py