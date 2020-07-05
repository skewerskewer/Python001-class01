# -*- coding: utf-8 -*-
import scrapy
from maoyan_movie.items import MaoyanmovieItem
from scrapy.selector import Selector


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']


#   注释默认的parse函数
#   def parse(self, response):
#        pass
    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
            url = 'https://maoyan.com/films?showType=3'
            # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        movies = Selector(response=response).xpath("//div[@class='movie-hover-info']")
        for movie in movies[0:10]:
            item = MaoyanmovieItem()
            name = movie.xpath('./div[1]/span/text()').extract()
            genre = movie.xpath('./div[2]/text()').extract()[1].strip('\n').strip()
            time = movie.xpath('./div[last()]/text()').extract()[1].strip('\n').strip()
            item.update({'name': name, 'genre': genre, 'time': time})
            yield item
