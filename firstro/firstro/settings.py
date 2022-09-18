# Scrapy settings for firstro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'firstro'

SPIDER_MODULES = ['firstro.spiders']
NEWSPIDER_MODULE = 'firstro.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = 'ERROR'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'shshshfp=eebbb2bba5ed808f2cf74ac04a1df067; shshshfpa=1b93245b-9987-86b0-8235-1fbfa6607b11-1661658873; shshshfpb=ddIlFZEKSz4TPbxdUZhX8vA; areaId=52993; __jdu=265529881; ipLoc-djd=52993-52994-53014-54727; unpl=JF8EAJBnNSttCkxWA08FHRJCQlhSW1oOTkQHbGVSAFsLQgABSQBOExR7XlVdXhRKHx9vZBRUXFNIUg4YCysSEXteVV5UD00QC2tkNWRaWEIZRElPKxEQe11Vbl4PTxMAZ24MVG1oTFQMKzIrFxBKXFNWWQFLEzNuVwdVXF1DVA0ZBxwiWyVcGV1aDE8UC2ZuBWRcaEg; CCC_SE=ADC_rsq9qW44goHc%2fMXZdC3FhPNDBzNPSZDBSvQksh1M%2bwf6EtRHamxogBaYlwBBcEMuBCwnH0z%2fzvNSbsv2gEr%2fRel5bcba5zQKAFaaleK4NtTwuc0vr%2be1oXlC%2bagxqJ%2fHBaeI3aGurMiA8CKXSzWCb1bMY3OtKPlI%2bQiQBYH9cSRxK26qrynCJlHKkA2hZLwVaBiG31xWPQQrNrQ61TLujPLTYxJkJoLue9CMBdoFE67GPcHrcBWMLMbPrPWtzJHMaPVRvQWQzIjIgClN4Nev%2fxR2Vu1OVGtNqWdKzA4xPtgDnlpgQkl1c52N6pKCWWTwf5rDSNV4xN3ObY6ULaPiC3xcBQbIL9D9P5PmYg53b6LWpN0aQoAAT8Kg79r0HlbHpI%2bGILPpuCR8N1oXhtummh8RfU6awNWe1wsbyKdbICyeuVS3xPAwF8UnE4zp%2bXe1x2AsIr9LM1Iom1pUSRvPpQ%3d%3d; __jdv=122270672|wjhsh.net|t_2018676952_|tuiguang|c637e671c8474674b523fe7b8e5c3d05|1662949649076; __jdc=122270672; jsavif=1; __jda=122270672.265529881.1661658870.1662949649.1663469141.3; ip_cityCode=2951; token=2e4d842f705a93d9059a05f66566ab63,2,924149; __tk=ArtujYfrkujE4zkpjVbqjz4wkUAqAzptjzayBVptAUn,2,924149; shshshsID=1bd45ad48f205f7987a6be227dfb460c_2_1663469167176; __jdb=122270672.2.265529881|3.1663469141; 3AB9D23F7A4B3C9B=5G27U7QJ7CB73IPSNX7PUDRHXRURIWUBYN6F2DXX2TTUUSYVKFGL4ELIWRQ532DUSHZNAM4ALBN5PPAVCRZFCZ7ND4',
    'referer': 'https://item.jd.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'firstro.middlewares.FirstroSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'firstro.middlewares.FirstroDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# # Configure item pipelines
# # See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
     'firstro.pipelines.FirstroPipeline': 300,
 }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
