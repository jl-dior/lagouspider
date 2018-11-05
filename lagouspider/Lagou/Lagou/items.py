# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.org/en/latest/topics/items.html

from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def handle_strip(value):
    return value.strip()


def replace_splash(value):
    return value.replace("/", "")

def handle_jobaddr(value):
    add_list = value.split("\n")
    add_list = [item.strip() for item in add_list if item.strip() != "查看地圖" ]
    return "".join(add_list)

class LagouItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class LagouItem(Item):
    collection = 'jl'

    title = Field()
    url = Field()
    salary = Field()
    job_city = Field(
        input_processor=MapCompose(replace_splash),
    )
    work_years = Field(
        input_processor=MapCompose(replace_splash),
    )
    degree_need = Field(
        input_processor=MapCompose(replace_splash),
    )
    job_type = Field()
    publish_time = Field()
    job_advantage = Field()
    job_desc = Field(
        input_processor=MapCompose(handle_strip),
    )
    job_addr = Field(
        input_processor=MapCompose(remove_tags, handle_jobaddr),
    )
    company_name = Field(
        input_processor=MapCompose(handle_strip),
    )
    company_url = Field()
    crawl_time = Field()
    crawl_update_time = Field()
