# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql


class FirstroPipeline(object):

    def open_spider(self,spider):
        print('开始爬虫……')


    def process_item(self, item, spider):
        user = item['user']
        content = item['content']
        times = item['times']

        # 创建数据库链接
        connector = pymysql.connect(
            host="localhost",
            user="root",
            password="040515Lzn",
            database="JDcomments",
            port=3306,
            charset='utf8'
        )


        cursor = connector.cursor()
        cursor.execute('USE JDcomments')

        cursor.execute(
            'INSERT INTO jdcoms VALUES (%s,%s,%s)',
            (user, content, times)
        )

        # 执行操作
        connector.commit()
        return item

    def close_spider(self,spider):
        print('爬虫结束！')




