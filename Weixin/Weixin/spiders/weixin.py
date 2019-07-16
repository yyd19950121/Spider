# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import WeixinItem


class WeixinSpider(CrawlSpider):
    name = 'weixin'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r".+article-.+\.html"),callback="parse_html",follow=False)
    )

    def parse_html(self, response):
        title = response.xpath('//h1[@class="ph"]/text()').get()
        author = response.xpath('//p[@class="authors"]/a/text()').get()
        time = response.xpath('//p[@class="authors"]/span/text()').get()
        content = response.xpath('//td[@id="article_content"]//text()').getall()
        content = ''.join(content)
        item = WeixinItem()
        item['title'] = title
        item['author'] = author
        item['time'] = time
        item['content'] = content
        print("ok!!!!")
        return item






