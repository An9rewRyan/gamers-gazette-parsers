import sys

# sys.path.append('/usr/src/utils/news_parser/scrapy_parser/spiders')
sys.path.append('D:\\game_news_parser\\main_parser\\spiders')
import scrapy
from main_spider import MainSpider

class DtfSpider(MainSpider):

    name = "dtf_site"
    start_urls = ['https://dtf.ru/gameindustry/entries/new']

    def __init__(self):
        self.link_path = "//a[@class= 'content-link']/@href"
        self.title_path = "//h1[@class='content-title']/descendant::text()[not(ancestor::span/@class='content-editorial-tick')]"
        self.subtitle = "//h1[@class='content-title']/span[1]/text()"
        self.text_path = '''//div[@class = 'content content--full ']/descendant::text()[ancestor::div/@class='l-island-a' and
                                                                                        not(ancestor::div/@class='andropov_link andropov_link--with_image') and 
                                                                                        not(ancestor::div/@class='content content--embed')] '''
        self.date_time_path = "//time[@class='time']/@title"
        self.image_path = '''//div[@class='content-image content-image--wide']/div[1]/@data-image-src |
                             //div[@class='content-image']/div[1]/@data-image-src'''
        self.site_base_link = "https://dtf.ru"
        self.site_name = 'dtf'

#to run: scrapy runspider dtf_spider.py