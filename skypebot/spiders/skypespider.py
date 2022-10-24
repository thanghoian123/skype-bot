
import json

import scrapy
from scrapy_selenium import SeleniumRequest


class SkypeBotSpider(scrapy.Spider):
    name = "skypebot"

    # def __init__(self, *args, **kwargs):
    #     # print("======self",self.start_urls)
    #     # url = kwargs.get('url').strip()
    #     # url_store = Selector(text=url).xpath('//text()').get()
    #     # print("--------url_store", url_store)

    #     self.url = 'http://shopeefood.vn/da-nang/ba-hon-ram-cuon-cai-pham-van-nghi.2zd82g'

    def start_requests(self):
        # print("--------self-url", self.url)
        urls= ['http://shopeefood.vn/da-nang/ba-hon-ram-cuon-cai-pham-van-nghi.2zd82g']
        for url in urls:
            yield SeleniumRequest(url=url, callback=self.parse, wait_time=10)

    # yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        print("=====vaoday")
        dict_product = []
        product_names = response.selector.css(
            '.item-restaurant-name::text').getall()
        print('---------product_names',product_names)
        # current-price
        product_prices = response.selector.css('.current-price::text').getall()
        for i in range(len(product_names)):
            dict_product.append(
                {'name': product_names[i], 'price': product_prices[i]})

        print(dict_product, "======dict_product")
        json_object = json.dumps(dict_product, indent=4)

        with open("sample.json", "w") as outfile:
            outfile.write(json_object)
