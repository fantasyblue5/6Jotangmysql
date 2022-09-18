# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from loguru import logger


class FirstroPipeline(object):
    fp = None
    def open_spider(self,spider):
        print('开始爬虫……')



    def process_item(self, item, spider):
        user = item['user']
        content = item['content']
        times = item['times']

        logger.info(item)

        with open('JDcomments.txt','a', encoding='utf-8') as f:
            f.write(user)
            f.write('\n')
            f.write(content)
            f.write('\n')
            f.write(times)
            f.write('\n')

        return item

    def close_spider(self,spider):
        print('爬虫结束！')

