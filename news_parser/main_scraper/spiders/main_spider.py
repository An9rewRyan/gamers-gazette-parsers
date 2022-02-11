
import scrapy
import time
import re

class MainSpider(scrapy.Spider):

    name = "sites"
    start_urls = ['example.com']
    rate = 1

    def __init__(self, link_path, title_path, text_path, date_time_path, image_path, site_name, site_base_link):
        
        self.link_path = link_path
        self.title_path = title_path
        self.text_path = text_path 
        self.date_time_path = date_time_path
        self.image_path = image_path
        self.site_name = site_name
        self.site_base_link = site_base_link

    def parse(self, response):

        links = response.xpath(self.link_path).getall()
        #проверка, является ли ссылка полной или сокращенной
        if self.site_base_link not in links[0]:
            for i in range(0, len(links)):
                links[i]=self.site_base_link+links[i]
        print(links)

        for link in links:
            yield scrapy.Request(url = link, callback = self.scrape)

    def scrape(self, response):

        title = self.format_title(response)
        text = response.xpath(self.text_path).getall()
        date_time = self.format_date_time(response)
        image = self.format_image(response)

        print(title, text, date_time, image, '\n\n\n\n\n\n\n\n\n')

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