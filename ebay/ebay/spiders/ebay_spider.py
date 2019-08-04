# -*- coding: utf-8 -*-
import scrapy
import re
import json
from ..items import EbayItem


class EbaySpiderSpider(scrapy.Spider):
    name = 'ebay_spider'
    allowed_domains = ["www.ebay-kleinanzeigen.de"]
    start_urls = ["https://www.ebay-kleinanzeigen.de/s-anzeige/s-klasse-w221-s500-v8-massage-keygo-magicbody-standhei-raten-kauf/1110949416-216-3411"]

    def parse(self, response):

        item = EbayItem()

        data = re.findall("bannerOpts: (.+?),\n    \n    contactPosterEnabled:", response.body.decode("utf-8"), re.S)
        ls = []
        if data:
            ls = json.loads(data[0])

        item["brand"] = ls["Marke"]
        item["car_type"] = ls["Fahrzeugtyp"]
        item["color"] = ls["Aussenfarbe"]
        item["fuel_type"] = ls["Kraftstoffart"]
        item["gear_type"] = ls["Getriebe"]
        item["mileage"] = ls["Kilometerstand"]
        item["model"] = ls["Modell"]
        item["price"] = ls["Preis"]
        item["ps"] = ls["Leistung__PS_"]
        item["year_of_registration"] = ls["Erstzulassungsjahr"]

        yield item





