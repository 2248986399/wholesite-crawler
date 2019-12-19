# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import os


def get_body(strs):
     return "\n\n".join([i for i in strs if i.strip()])
        

md_tmp = '''---
layout: default
title: "{}"
date: {}
---

{}

'''

class LetsCoprSpider(scrapy.Spider):
    name = 'letscorp'
    allowed_domains = ['s3.amazonaws.com']
    host = "https://s3.amazonaws.com/letscorp-archive/"
    start_urls = ['https://s3.amazonaws.com/letscorp-archive/index.html']

    def parse(self, response):
        url = response.url
        if len(url.split("/")[-1]) > 2:
            title = response.css("header h2 ::text").extract()[1]
            body = get_body( response.css(".entry-content ::text").extract() )
            date = response.css("time::attr(datetime)").extract()[0].replace("+",".000000+")
            tmp = md_tmp.format(title, date, body)
            dir = "./post"
            if not os.path.exists(dir):
                os.makedirs(dir)
            with open("{}/{}.md".format(dir,title), 'wb') as f:
                f.write( tmp.encode() )
        for post in response.css("td a::attr(href)").extract():
            yield scrapy.Request(post,self.parse)
        for page in response.css("h2 a::attr(href)").extract():
            yield scrapy.Request(page,self.parse)