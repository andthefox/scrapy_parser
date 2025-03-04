import scrapy


class InstaParseItem(scrapy.Item):
    likes = scrapy.Field()
    comments = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    description = scrapy.Field()
