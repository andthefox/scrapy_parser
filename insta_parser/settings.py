BOT_NAME = 'insta_parser'

SPIDER_MODULES = ['insta_parser.spiders']
NEWSPIDER_MODULE = 'insta_parser.spiders'

ROBOTSTXT_OBEY = False

FEEDS = {
    'results/insta_reels_%(time)s.csv': {
        'format': 'csv',
        'fields': ['likes', 'comments', 'author', 'date', 'description'],
        'overwrite': True
    },
}
FEED_EXPORT_ENCODING = 'utf-8'

ITEM_PIPELINES = {
    'insta_parser.pipelines.InstaParsePipeline': 300,
}

LOG_FILE = 'scrapy_output.txt'
