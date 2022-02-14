import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# sys.path.append('D:\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\spiders')
sys.path.append('D:\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\utils')
# sys.path.append('D:\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\formatters')
from scrapy_selenium import SeleniumRequest
from post_formatter import format_post
import scrapy
import time
import re

class MainSpider(scrapy.Spider):

    name = "sites"
    start_urls = ['example.com']
    rate = 1
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': '\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\scraped_data\\data.json',
        'FEED_EXPORT_ENCODING' : 'utf-8'
    }

    def __init__(self, link_path, title_path, text_path, date_time_path, image_path, site_name, site_base_link):
        
        self.link_path = link_path
        self.title_path = title_path
        self.text_path = text_path 
        self.date_time_path = date_time_path
        self.image_path = image_path
        self.site_name = site_name
        self.site_base_link = site_base_link

    def parse(self, response):
        print(response.request.url)
        yield SeleniumRequest(url=response.request.url, wait_time=10, wait_until=EC.element_to_be_clickable((By.CLASS_NAME, 'knb-grid-container')), callback=self.parse_links)
#         links = response.xpath(self.link_path).getall()
#         print(links)
#         #проверка, является ли ссылка полной или сокращенной
#         if self.site_base_link not in links[0]:
#             for i in range(0, len(links)):
#                 links[i]=self.site_base_link+links[i]
# # KnbPageTitle_title__RbUh8
#         for link in links:
#             yield SeleniumRequest(url = link, callback = self.scrape)
    def parse_links(self, response):

        links = response.xpath(self.link_path).getall()
        print('Здесь!')
        print(links)
        #проверка, является ли ссылка полной или сокращенной
        if self.site_base_link not in links[0]:
            for i in range(0, len(links)):
                links[i]=self.site_base_link+links[i]
        # KnbPageTitle_title__RbUh8
        for link in links:
            if 'reviews' in link:
                continue
            yield scrapy.Request(url = link, callback = self.scrape)

    def scrape(self, response):

        title = self.format_title(response)
        text = response.xpath(self.text_path).getall()
        date_time = self.format_date_time(response)
        image = self.format_image(response)

        post = {
            'title': title,
            'text': text,
            'date_time': date_time,
            'image': image
        }

        post = format_post(post)

        yield {'title':post["title"], 'pub_date':post["date_time"], 'image':post["image"], 'text':post["text"]}

    def format_image(self, response):
        image = response.xpath(self.image_path).get(default="https://upload.wikimedia.org/wikipedia/commons/a/a3/Image-not-found.png")
        if "https://" not in image:
            image=self.site_base_link+image
        return image
    
    def format_date_time(self, response):
        date_time = response.xpath(self.date_time_path).get()
        return date_time
    
    def format_title(self, response):
        title = response.xpath(self.title_path).getall()
        return title