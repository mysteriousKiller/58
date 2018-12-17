# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
# 导入随机模块
import random
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class WubaSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WubaDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# IP池
# class HTTPPROXY(HttpProxyMiddleware):
#     # 初始化 注意一定是 ip=''
#     def __init__(self, ip=''):
#         self.ip = ip
#
#     def process_request(self, request, spider):
#         item = random.choice(IPPOOL)
#         try:
#             print("当前的IP是："+item["ipaddr"])
#             request.meta["proxy"] = "http://"+item["ipaddr"]
#         except Exception as e:
#             print(e)
#             pass


# 设置IP池
IPPOOL = [
    {"ipaddr": "222.92.85.37"},
    {"ipaddr": "125.117.135.223"},
    {"ipaddr": "119.163.135.143"},
    {"ipaddr": "163.125.115.91"},
    {"ipaddr": "118.24.98.96"},
    {"ipaddr": "114.95.142.55"},
    {"ipaddr": "115.231.5.230"},
    {"ipaddr": "115.223.213.221"},
    {"ipaddr": "118.182.33.6"},
    {"ipaddr": "180.118.73.207"},
    {"ipaddr": "124.235.181.175"},
    {"ipaddr": "112.74.73.134"},
    {"ipaddr": "140.207.25.114"},
    {"ipaddr": "58.251.49.4"},
    {"ipaddr": "117.90.137.2"}
]


# 用户代理
class USERAGENT(UserAgentMiddleware):
    #初始化 注意一定是 user_agent=''
    def __init__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        item = random.choice(UPPOOL)
        try:
            print("当前的User-Agent是："+item)
            request.headers.setdefault('User-Agent', item)
        except Exception as e:
            print(e)
            pass


# 设置用户代理池
UPPOOL = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
]