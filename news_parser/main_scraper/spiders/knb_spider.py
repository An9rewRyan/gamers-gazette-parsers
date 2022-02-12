import sys
sys.path.append('D:\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\spiders')
sys.path.append('D:\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\utils')
import scrapy
from main_spider import MainSpider
from get_json_from_script_tag import get_info_from_json
import json

class KnbSpider(MainSpider):

    name = "knb"
    start_urls = ['https://kanobu.ru/videogames/']

    def __init__(self):
        self.link_path = "//main/a"
        self.title_path = "//script[@type='application/ld+json']/text()"
        self.text_path = "//div[starts-with(@class, 'material-content')]/descendant::text()[not(ancestor::ul)]"
        self.date_time_path = "//script[@type='application/ld+json']/text()"
        self.image_path = "//link[@rel='preload'][@as='image']/@href"
        self.site_name = 'knb'
        self.site_base_link = 'https://kanobu.ru'

    def parse(self, response):
        landing_data = response.xpath("//script[@id='__NEXT_DATA__']").get()
        posts_data = get_info_from_json(landing_data, "props","initialStoreState","headingPageStore","materials","results")
        for post in posts_data:
            url = "https://kanobu.ru/news/"+post["slug"]+"-"+str(post["id"])+'/'
            yield scrapy.Request(url = url, callback = self.scrape)

    def format_date_time(self, response):
        date_time = super(KnbSpider, self).format_date_time(response)
        date_time = json.loads(date_time)["datePublished"]
        return date_time
    
    def format_title(self, response):
        title = super(KnbSpider, self).format_title(response)
        title = json.loads(title[0])["headline"]
        return title

# to run: scrapy runspider knb_spider.py
