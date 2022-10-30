

import json

import scrapy
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SkypeBotSpider(scrapy.Spider):
    name = "skypebot"

    def __init__(self, *args, **kwargs):
        # print("======self",self.start_urls)
        # dispatcher.connect(self.spider_closed, signals.spider_closed)
        url = kwargs.get('url').strip()
        url_store = Selector(text=url).xpath('//text()').get()
        print("--------url_store", url_store)
        self.url = url_store

    def start_requests(self):
        print("--------self-url", self.url)
        urls= ['http://shopeefood.vn/da-nang/ba-hon-ram-cuon-cai-pham-van-nghi.2zd82g']
        for url in urls:
            yield SeleniumRequest(url=url, callback=self.parse, wait_time=10, 
            wait_until=EC.element_to_be_clickable((By.CLASS_NAME, 'item-restaurant-row')))

    # yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        print("=====vaoday")
        print(response.body)
        dict_product = []
        product_names = response.selector.css(
            '.item-restaurant-name::text').getall()
        # current-price
        product_prices = response.selector.css('.current-price::text').getall()
        for i in range(len(product_names)):
            dict_product.append(
                {'name': product_names[i], 'price': product_prices[i]})
        json_object = json.dumps(dict_product, indent=4)

        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
    def spider_closed(self, spider):
        print("----------------end")
