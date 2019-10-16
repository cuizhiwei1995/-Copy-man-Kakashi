# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import re
class ZhihuPipeline(object):
    def process_item(self, item, spider):
        if type(item).__name__ == 'AnswerItem':
            title = item['title']
            # 设置保存的文件名，把子链接去掉'http://'和'.shtml'，把'/'替换成‘_’，保存为txt文件格式
            new_title = ''.join(title)
            new_title = re.sub("[^0-9A-Za-z\u4e00-\u9fa5]", '', new_title)
            content = item['content']
            content = ''.join(content)
            content = re.sub(r'<.*?>', '', content)
            content = re.sub(r'\s', '', content)
            self.filename = new_title + '.txt'
            filename = 'F:\\projects\\practise\\100W\\{}'.format(self.filename)

            self.file = open(filename, 'w',encoding='utf-8')

            self.file.write(content)
            self.file.close()
