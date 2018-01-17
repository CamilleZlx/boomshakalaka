#!/usr/bin/env python
#_*_ coding: utf-8 _*_
# python = 3.6.2
from suds.client import Client
import importlib
import sys
importlib.reload(sys)
user_url = "http://apis.map.qq.com/ws/place/v1/suggestion/?region=北京&keyword=美食" \
           "&key=NYDBZ-6DACO-O7YWB-S7YXL-XCZ43-MVFLP"
client = Client(user_url)

print(client)



