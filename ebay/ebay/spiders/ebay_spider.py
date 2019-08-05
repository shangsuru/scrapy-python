# -*- coding: utf-8 -*-
import scrapy
import re
import json
from ..items import EbayItem


class EbaySpiderSpider(scrapy.Spider):
    name = "ebay_spider"
    page_number = 2
    base_url = "https://www.ebay-kleinanzeigen.de/"
    allowed_domains = ["www.ebay-kleinanzeigen.de"]
    start_urls = ["https://www.ebay-kleinanzeigen.de/s-autos/seite:1/c216"]

    def parse(self, response):

        links = response.css("a.ellipsis::attr(href)").extract()
        for link in links:
            yield scrapy.Request(EbaySpiderSpider.base_url + link, callback = self.parse_listing)

        next_page = "https://www.ebay-kleinanzeigen.de/s-autos/seite:" + str(EbaySpiderSpider.page_number) + "/c216"
        if EbaySpiderSpider.page_number <= 50:
            EbaySpiderSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)

    def parse_listing(self, response):
        item = EbayItem()

        data = re.findall("bannerOpts: (.+?),\n    \n    contactPosterEnabled:", response.body.decode("utf-8"), re.S)
        ls = []
        if data:
            ls = json.loads(data[0])

        item["brand"] = ls.get("Marke", "")
        item["car_type"] = ls.get("Fahrzeugtyp", "")
        item["color"] = ls.get("Aussenfarbe", "")
        item["fuel_type"] = ls.get("Kraftstoffart", "")
        item["gear_type"] = ls.get("Getriebe", "")
        item["mileage"] = ls.get("Kilometerstand", "")
        item["model"] = ls.get("Modell", "")
        item["price"] = ls.get("Preis", "")
        item["ps"] = ls.get("Leistung__PS_", "")
        item["year_of_registration"] = ls.get("Erstzulassungsjahr", "")

        yield item





