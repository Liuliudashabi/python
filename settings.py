# -*- coding: utf-8 -*-

# Scrapy settings for tack project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tack'

SPIDER_MODULES = ['tack.spiders']
NEWSPIDER_MODULE = 'tack.spiders'

ITEM_PIPELINES = {
   'tack.pipelines.JsonWithEncodingCnblogsPipeline': 300,
}
LOG_LEVEL = 'INFO'
