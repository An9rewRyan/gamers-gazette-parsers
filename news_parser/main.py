import sys

sys.path.append('D:\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\spiders')
sys.path.append('D:\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\utils')
sys.path.append('D:\\gamers_gazette_parsers\\gamers-gazette-parsers\\news_parser\\main_scraper\\formatters')

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from dtf_spider import DtfSpider
from vg_spider import VgSpider
from sg_spider import SgSpider
from pgd_spider import PgdSpider
from knb_pider import KnbSpider
from igrm_spider import IgrmSpider
from celery import Celery

app = Celery('main',broker='redis://redis-server:6379/0')

process = CrawlerProcess()

@app.task
def renew_db():

    process.crawl(DtfSiteSpider)
    process.crawl(VgSiteSpider)
    process.crawl(SgSiteSpider)
    process.crawl(PgdSiteSpider)
    process.crawl(KnbSiteSpider)
    process.crawl(IgrmSiteSpider)
    process.start()

app.conf.beat_schedule = {
 'renew-db-me-every-10-minutes': {
 'task': 'main.renew_db',
 'schedule': 600.0
 }
}