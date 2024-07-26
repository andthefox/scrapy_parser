import csv
from csv import excel
from datetime import datetime

BASE_DIR = './results'


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counter = dict()
        self.total = 0

    def process_item(self, item, spider):
        self.status_counter[item['status']] = (
            self.status_counter.get(item['status'], 0) + 1
        )
        self.total += 1
        return item

    def close_spider(self, spider):
        self.status_counter['Total'] = str(self.total)

        time = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")
        filename = f'{BASE_DIR}/status_summary_{time}.csv'

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, dialect=excel)
            writer.writerow(('Статус', 'Количество'))
            writer.writerows(self.status_counter.items())
