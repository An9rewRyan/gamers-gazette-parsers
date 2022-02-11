import sys

# sys.path.append('/usr/src/utils/news_parser/scrapy_parser/spiders')
sys.path.append('D:\\game_news_parser\\main_parser\\spiders')
import scrapy
from main_spider import MainSpider
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
        begin_of_json_index = landing_data.find('>')
        end_of_json_index = landing_data.find('</')
        landing_data = landing_data[begin_of_json_index+1:end_of_json_index]
        landing_data_json = json.loads(landing_data)
        posts_data = landing_data_json["props"]["initialStoreState"]["headingPageStore"]["materials"]["results"]
        for post in posts_data:
            url = "https://kanobu.ru/news/"+post["slug"]+"-"+str(post["id"])+'/'
            yield scrapy.Request(url = url, callback = self.scrape)

    def format_date_time(self, response):
        date_time = super(KnbSpider, self).format_date_time(response)
        date_time_json = json.loads(date_time)
        date_time = date_time_json["datePublished"]
        return date_time
    
    def format_title(self, response):
        title = super(KnbSpider, self).format_title(response)
        title = title[0]
        title_json = json.loads(title)
        title = title_json["headline"]
        return title

