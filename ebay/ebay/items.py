# -*- coding: utf-8 -*-

import scrapy


class EbayItem(scrapy.Item):
    brand = scrapy.Field()
    car_type = scrapy.Field()
    color = scrapy.Field()
    fuel_type = scrapy.Field()
    gear_type = scrapy.Field()
    mileage = scrapy.Field()
    model = scrapy.Field()
    price = scrapy.Field()
    ps = scrapy.Field()
    year_of_registration = scrapy.Field()




