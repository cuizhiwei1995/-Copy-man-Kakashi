# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from .UserAgent import agents
import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware #UserAegent中间件
class UserAgentmiddleware(UserAgentMiddleware):

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers['Referer']='https://www.zhihu.com'
        request.headers["User-Agent"] = agent
        return None

