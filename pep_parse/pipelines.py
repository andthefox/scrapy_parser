import csv
from datetime import datetime

BASE_DIR = '/results'


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
        time = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")
        with open(
            f'{BASE_DIR}/status_summary_{time}.csv',
            'w',
            newline='',
            encoding='utf-8'
        ) as csvfile:
            writer = csv.writer(
                csvfile, delimiter=','
            )
            writer.writerow(('Статус', 'Количество'))
            for status, quantity in self.status_counter.items():
                writer.writerow((status, quantity))
            writer.writerow(('Total', str(self.total)))
