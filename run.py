# from scrapy import cmdline
# cmdline.execute(['scrapy', 'crawl', "Job51"])
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from Job_51Spider.spiders.job51 import Job51Spider

settings = get_project_settings()
process = CrawlerProcess(settings=settings)
# 可以添加多个spider
process.crawl(Job51Spider)
# 启动爬虫，会阻塞，直到爬取完成
process.start()