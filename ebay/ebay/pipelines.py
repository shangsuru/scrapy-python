# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class EbayPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("cars.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS car_listings""")
        self.curr.execute("""CREATE TABLE car_listings(
                        brand TEXT,
                        car_type TEXT,
                        color TEXT,
                        fuel_type TEXT,
                        gear_type TEXT,
                        mileage INTEGER,
                        model TEXT,
                        price INTEGER,
                        ps INTEGER,
                        year_of_registration INTEGER
                        )""")

    def store_db(self, item):
        self.curr.execute("""INSERT INTO car_listings VALUES (?,?,?,?,?,?,?,?,?,?)""", (
                                item["brand"],
                                item["car_type"],
                                item["color"],
                                item["fuel_type"],
                                item["gear_type"],
                                item["mileage"],
                                item["model"],
                                item["price"],
                                item["ps"],
                                item["year_of_registration"]
                                ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item


