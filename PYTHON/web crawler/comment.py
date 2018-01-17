# coding=utf-8

import urllib2
import sys
import json
import re

# 设置系统默认编码为utf-8
reload(sys)
sys.setdefaultencoding("utf-8")

# Only for python2
'''
只是简单的示例，没有检查无评论的情况，其它异常也可能没有检查，
你可以根据自己的需要再对代码修改
'''


# 解析网页数据
def parseData(html_data, reg_str):
    pattern = re.compile(reg_str)
    result = re.search(pattern, html_data)
    if result:
        return result.groups()


# commodity_url 为商品详情页面
commodity_url = "http://item.taobao.com/item.htm?spm=a1z10.1-c.w4004-9140345655.2.y3LCj0&id=44454286657"

html_data = urllib2.urlopen(commodity_url).read()
# 获取用户ID和商品ID
auction_msg = parseData(html_data, r'userNumId=(.*?)&auctionNumId=(.*?)&')
if not auction_msg:
    print "Get reviews failed!"  # 获取失败，退出
    sys.exit()

reviews_url = "https://detail.tmall.com/item.htm?id=18064323239&ad_id=&am_id=&cm_id=140105335569ed55e27b&pm_id=&abbucket=2" % auction_msg

response = urllib2.urlopen(reviews_url)
reviews_data = response.read().decode("gbk")

# 获取评论数据
json_str = parseData(reviews_data, r'\((.*)\)')[0]
if not json_str:
    print "Get reviews failed!"  # 获取失败，退出
    sys.exit()

jdata = json.loads(json_str)

# 下面只打印了第一条评论，如需要打印所有，则遍历jdata["comments"]即可
print jdata["comments"][0]["content"]