# -*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import Selector,HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from tack.items import TackItem
from scrapy.http import Request
class StackSpider(BaseSpider):
    name = "tack"
    allowed_domains = ["guba.eastmoney.com"]
    start_urls = ["http://guba.eastmoney.com/list,600482_1.html"]
    rules = [
        Rule(SgmlLinkExtractor(allow=(r'http://guba.eastmoney.com/default_1.html\?start=\d+.*'))),
        Rule(SgmlLinkExtractor(allow=(r'http://guba.eastmoney.com/subject/\d+')), callback="parse_item"),
    ]
    for i in range (1,1157,1):
        start_urls.append('http://guba.eastmoney.com/list,600482_%d.html'%i)
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('/html/body[@class="hlbody"]/div[@class="gbbody"][5]/div[@id="mainbody"]/div[@id="articlelistnew"]/div[@class="articleh"]')
        items = []
        for site in sites:
            item = TackItem()
            item['title'] = site.select('span[@class="l3"]/a/text()').extract()
            item['url'] = site.select('span[@class="l3"]/a/@href').extract()
            item['rtimes']=site.select('span[@class="l1"]/text()').extract()
            item['ctimes'] = site.select('span[@class="l2"]/text()').extract()
            items.append(item)
        return items

