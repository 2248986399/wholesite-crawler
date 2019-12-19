# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


md_tmp = '''---
layout: default
title: "{}"
weight: {}
---

{}

{}

'''

class CcradbSpider(scrapy.Spider):
    name = 'ccradb'
    allowed_domains = ['ccradb.appspot.com']
    host = "http://ccradb.appspot.com"
    start_urls = ['http://ccradb.appspot.com/page/1']

    def parse(self, response):
        print(response.url)
        if "post" in response.url:
            weight = response.url.split("/")[-1]
            title = weight + "."+ response.css(".title ::text").extract_first().strip()
            date = "".join( [i.strip() for i in response.css(".sub_title ::text").extract()[1:]] )
            body = "\n\n".join( list( filter(lambda x: len(x) > 0, [i.strip() for i in response.css(".custom-richtext ::text").extract()] )) )
            with open("./post/{}.md".format(weight), 'wb') as f:
                tmp = md_tmp.format(title,weight , date, body)
                f.write( tmp.encode() )
        for post in response.css(".stitle a::attr(href)").extract():
            yield scrapy.Request(self.host + post,self.parse)
        for page in response.css(".pagination a::attr(href)").extract():
            yield scrapy.Request(self.host + page,self.parse)

