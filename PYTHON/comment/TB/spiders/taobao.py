# -*- coding: utf-8 -*-
# python 3.6

import scrapy
import socket
import time
from scrapy import selector
from selenium import webdriver
from TB.items import TbItem
from urllib.parse import urlparse, parse_qs
from selenium.webdriver.support.ui import WebDriverWait
import glob
from scrapy import Request, Selector

#读取URL
#txt_filenames = glob.glob('C:\\Users\\Camille\\Desktop\\Python3\\*.txt') #test
txt_filenames = glob.glob('.\\documents\\URL_data_output\\*.txt') #data

urlData = []
for filename in txt_filenames:
      txt_file = open(filename, 'r',encoding = 'utf-8')
      #print(txt_file)
      lines = txt_file.readlines()
      for line in lines :
         # print(line)
          temp = line.replace('\n','')
          #print(temp)
          urlData.append(temp.replace('\ufeff',''))
# start_URL = urlData
# print(start_URL)
# print(urlData)

def login_taobao(login=False):
    chromeOptions = webdriver.ChromeOptions()
    # 开启无头浏览器功能，现在貌似不好用
    # chromeOptions.add_argument("--headless")
    # chromeOptions.add_argument("--disable-gpu")

    prefs = {"profile.managed_default_content_settings.images": 2}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)

    if login:
        # driver.maximize_window()
        driver.delete_all_cookies()
        driver.get("https://login.taobao.com/member/login.jhtml")
        element = WebDriverWait(driver, 60).until(lambda dv: dv.find_element_by_xpath("//*[@id='J_Quick2Static']"))
        element.click()
        driver.implicitly_wait(20)
        username = driver.find_element_by_name("TPL_username")
        if not username.is_displayed():
            driver.implicitly_wait(20)
            driver.find_element_by_xpath("//*[@id='J_Quick2Static']").click()
        driver.implicitly_wait(20)
        password = driver.find_element_by_name("TPL_password")
        username.send_keys("TB啊啊啊哈哈哈") # 在此填入淘宝账号
        password.send_keys("123456qweA") # 在此填入淘宝密码
        time.sleep(10)
        driver.implicitly_wait(20)
        #driver.find_element_by_xpath("//*[@id='J_SubmitStatic']").click()
        time.sleep(4)

    driver.set_page_load_timeout(30)
    return driver



class TaobaoSpider(scrapy.Spider):
    name = "taobao"
    allowed_domains = ["taobao.com"]
    start_urls = urlData
    # start_urls = ['https://item.taobao.com/item.htm?id=9460519723&ns=1&abbucket=13#detail',
    #               'https://item.taobao.com/item.htm?id=550132815374&ns=1&abbucket=13#detail',
    #               'https://item.taobao.com/item.htm?id=547932047840&ns=1&abbucket=13#detail',
    #               'https://item.taobao.com/item.htm?id=550109646527&ns=1&abbucket=13#detail',
    #               'https://item.taobao.com/item.htm?id=36361274627&ns=1&abbucket=13#detail']

    def __init__(self, *args, **kwargs):
        super(TaobaoSpider, self).__init__(*args, **kwargs)
        self.driver = None
        self.driver = login_taobao(True)
        # chromeOptions = webdriver.ChromeOptions()
        # prefs = {"profile.managed_default_content_settings.images":2}
        # chromeOptions.add_experimental_option("prefs",prefs)
        # self.driver = webdriver.Chrome(chrome_options = chromeOptions)

        # 使用无界面浏览器 PhantomJS
        # service_args = ['--load-images=no', '--disk-cache=yes', '--ignore-ssl-errors=true']
        # self.driver = webdriver.PhantomJS(service_args=service_args)
        # self.driver.set_page_load_timeout(30)
        # self.driver.implicitly_wait(10)

    def parse(self, response):
        self.driver.get(response.url)
        # self.driver.implicitly_wait(30)
        selector = Selector(text=self.driver.page_source)

        for sel in selector.xpath('//*[@id="J_Counter"]'):
            item = TbItem()
            #item['item_name'] = sel.xpath('//*[@id="J_Title"]/h3/text()').extract_first()
            item['item_name'] = sel.xpath('//*[@id="J_Title"]/h3/@data-title').extract_first().replace(",","，").replace("\n","。")
            item['item_id'] = parse_qs(urlparse(response.url).query, True)['id'][0].replace(",","，").replace("\n","。")
            item['comments'] = sel.xpath('//*[@id="J_RateCounter"]/text()').extract_first().replace(",","，").replace("\n","。")
            item['trade'] = sel.xpath('//*[@id="J_SellCounter"]/text()').extract_first().replace(",","，").replace("\n","。")
            item['price'] = sel.xpath('//*[@id="J_StrPrice"]/em[2]/text()').extract_first().replace(",","，").replace("\n","。")
            yield item

    def __del__(self):
        if self.driver is not None:
            self.driver.quit()
