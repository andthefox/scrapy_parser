import csv
from csv import excel
from datetime import datetime

BASE_DIR = './results'


class InstaParsePipeline:
    def open_spider(self, spider):
        self.total = 0

    def process_item(self, item, spider):
        self.total += 1
        return item

    def close_spider(self, spider):
        print('Всего обработано ссылок:', str(self.total))
