# -*- coding: utf-8 -*-

# Scrapy settings for wuba project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wuba'

SPIDER_MODULES = ['wuba.spiders']
NEWSPIDER_MODULE = 'wuba.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wuba (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
#     'Cookie': 'id58=c5/nn1vqT45QYl4ryy/4Ag==; __utma=253535702.1410368820.1542082444.1542082444.1542082444.1; __utmz=253535702.1542082444.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; 58tj_uuid=bc0e5697-d99a-4659-b4a6-0f45e6c26ff5; myfeet_tooltip=end; gr_user_id=295c893e-dd2a-4b7a-a64e-277e4a85e60e; wmda_uuid=184988cea2774584c132832ceb8615d2; wmda_new_uuid=1; wmda_visited_projects=%3B1409632296065; _ga=GA1.2.1410368820.1542082444; als=0; 58home=cn; xxzl_deviceid=dxAyHCjiLhmpkEW1DqVKsSKS6%2BjlwPKKwxHCbwuI7jEDnQgJjtoED605QNpz9y7R; sessionid=205d51f8-cc9c-4b56-8f3b-a27b00fcf872; Hm_lvt_3bb04d7a4ca3846dcc66a99c3e861511=1542082567,1542272417; Hm_lvt_e15962162366a86a6229038443847be7=1542082568,1542272419; Hm_lvt_e2d6b2d0ec536275bb1e37b421085803=1542273196; Hm_lpvt_e2d6b2d0ec536275bb1e37b421085803=1542277315; final_history=28972791289773%2C30720333282366%2C30458760904528%2C33870828015695%2C32865744139054; ppStore_fingerprint=524130B44C4E95D8092B51D9C9AE51CD610866727F7F57BD%EF%BC%BF1542277317968; _gid=GA1.2.1492984764.1542589612; f=n; commontopbar_new_city_info=122%7C%E9%9D%92%E5%B2%9B%7Cqd; commontopbar_ipcity=fs%7C%E4%BD%9B%E5%B1%B1%7C0; Hm_lpvt_3bb04d7a4ca3846dcc66a99c3e861511=1542613083; Hm_lpvt_e15962162366a86a6229038443847be7=1542613084; xzfzqtoken=uGulyQIoU4K57prCIpHWWuswLF1Tx4Ymy8dwWyo9TMjIq5pt3sEoFpRAt78H9MP0in35brBb%2F%2FeSODvMgkQULA%3D%3D; city=hf; new_uv=6; GA_GTID=0d20678d-0034-5e58-63a9-5f1dcc83e5d6',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wuba.middlewares.WubaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'wuba.middlewares.WubaDownloaderMiddleware': 543,
  'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 2,
  'wuba.middlewares.USERAGENT': 1
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'wuba.pipelines.WubaPipeline': 100,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
