# -*- coding: utf-8 -*-
import scrapy
import requests
import http.cookiejar
from zhihu.items import AnswerItem
import json
from urllib.parse import urlencode
from  scrapy_redis.spiders import RedisSpider

class ZhSpider(RedisSpider):
    name = 'zh'
    redis_key = "ZhSpider:start_urls"
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    #     "Referer": "https://www.zhihu.com",
    # }


    # def start_requests(self):
        # login=ZhihuAccount('15044957421', 'czw1995happy')
        # login.login(captcha_lang='en', load_cookies=True)

        # yield scrapy.FormRequest(url='https://www.zhihu.com/', cookies=self
        #                          .COOKIE_VALUE, dont_filter=True, method='GET',
        #                          callback=self.parse)

    # def parse(self, response):
    #     cookie1 = http.cookiejar.LWPCookieJar()
    #     cookie1.load('F:\\projects\\practise\\zhihu\\zhihu\\cookie\\cookies.txt')
    #     # 从文件中读取cookies
    #     self.COOKIE_VALUE = requests.utils.dict_from_cookiejar(cookie1)
    #     start = 0
    #     end = 100000000
    #     for i in range(start,end):
    #
    #         params = {
    #             'session_token': '4975ba96688e66562b3a4d2d4cfa5185',
    #             'desktop': 'true',
    #             'page_number': start,  # 地址中有2个变量page_number和after_id,但这2个数据有关联
    #             'limit': '6',
    #             'action': 'down',
    #             'after_id': int(start) * 6 - 7
    #         }
    #         base_url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend?'
    #         # 接口网址的前边地址
    #         url = base_url + urlencode(params)  # 拼接地址
    #         print(url)
    #         start=start+1
    #         print("====!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!===={}".format(start))
    #         yield scrapy.Request(url, cookies=self.COOKIE_VALUE, callback=self.get_data,dont_filter=True)
    #
    def get_data(self, response):
        answer_item = AnswerItem()
        result = json.loads(response.text)
        data_list = result.get('data')
        if data_list:
            print("=====$$$$$$$$$$$$$$$$$$$$$$$$$$$===={}".format(len(data_list)))
            for item in data_list:  # 遍历items,获取0-5下的数据
                item = item.get('target') # 定位到问题那一栏
                if item:  # 先判断能不能拿到item
                    try:
                        titles = item.get('question').get('title') # 知乎问题标题
                        if titles:
                            content = item.get('content')  # 知乎问题id
                            answer_item['content'] = content
                            answer_item['title'] = titles
                            yield answer_item
                    except:
                        pass


