import sys

# sys.path.append('/usr/src/utils/news_parser/scrapy_parser/spiders')
sys.path.append('D:\\game_news_parser\\main_parser\\spiders')
import scrapy
from main_spider import MainSpider

class IgrmSpider(MainSpider):

    name = "igrm_site"
    start_urls = ['https://www.igromania.ru/news/game/']

    def __init__(self):
        self.link_path = "//a[@class='aubli_img']/@href"
        self.title_path = "//h1[@class ='page_news_ttl haveselect']/text()"
        self.text_path = '''//div[@class = 'universal_content clearfix']/descendant::text()[(ancestor::div[not(@class)] or ancestor::li) and 
                                                                                            not(ancestor::div[@class='uninote console'])]'''
        self.date_time_path = "//div[@class='page_news noselect']/meta[@itemprop = 'datePublished']/@content"
        self.image_path = "//div[@class ='main_pic_container']/img/@src"
        self.site_base_link = "https://www.igromania.ru"
        self.site_name = 'igrm'

# to run: scrapy runspider igrm_spider.py