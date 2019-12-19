# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from datetime import datetime
import re,os

def parse_date(str):
    try:
        return datetime.strptime(str, "%y.%m.%d").strftime("%Y-%m-%dT%H:%M:%S.%f+08:00")
    except:
        return False

def get_title(str):
    try:
        if len(str[0].strip()) > 40:
            return str[0].strip()[:40]
        return str[0].strip()
    except:
        return ""

def get_author(str):
    try:
        for i in str[1].split(" "):
            if "作者：" in i:
                return i.replace("作者：","").strip()
            if "方舟子" in i:
                return "方舟子"
        return ""
    except:
        return ""

md_tmp = '''---
layout: default
title: '{}'
date: {}
author:
    display_name: {}
---

{}

'''

class XysSpider(scrapy.Spider):
    name = 'xys'
    allowed_domains = ['www.xys.org']
    host = "http://www.xys.org/"
    start_urls = ['http://www.xys.org/']

    def parse(self, response):
        url = response.url
        date = response.meta.get("date", None)
        if date:
            
            body = response.body.decode(response.encoding).split("\n\n")[1:-1]

            title = get_title(body)
            author = get_author(body).split("\n")[0]

            body = "\n\n".join([i.strip().replace("\n","") for i in body])
            filename = response.url.split("/")[-1].replace(".txt","")
            tmp = md_tmp.format(title, date, author, body)
            dir = "./post"
            if not os.path.exists(dir):
                os.makedirs(dir)
            with open("{}/{}.md".format(dir,filename), 'wb') as f:
                f.write( tmp.encode() )
        for item in response.css("li").extract():
            link = Selector(text=item).css("li a::attr(href)").extract_first()
            if link:
                if "netters" in link or "ebooks" in link:
                    date  = Selector(text=item).css("li ::text").extract_first().strip().replace(",","")
                    date = parse_date(date)
                    yield scrapy.Request(self.host + link,self.parse, meta={"date":date})

                if "new" in link and ".html" in link:
                    yield scrapy.Request(self.host + link,self.parse)

            

