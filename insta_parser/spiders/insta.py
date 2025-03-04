import csv
import scrapy

from tqdm import tqdm

LIST_FILE = 'list.csv'


# Instagram - продукт компании Meta, признанной экстремистской в РФ


class InstaSpider(scrapy.Spider):
    name = 'insta'
    allowed_domains = ['instagram.com', 'www.instagram.com']
    start_urls: list[str] = []

    def __init__(self, name=None, **kwargs):
        with open(LIST_FILE, mode='r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                self.start_urls.append(str(row[0]))
        super().__init__(name, **kwargs)

    def parse(self, response):
        """
        Собирает ссылки на рилсы и запускает парсинг
        """

        for link in tqdm(self.start_urls):
            yield response.follow(link, callback=self.parse_reel)

    def parse_reel(self, response):
        """
        Парсит страницы с документами, формирует Items
        """
        description = response.xpath(
            "//meta[@name='description']/@content"
        ).getall()
        metadata = ' '.join(description).split('"')[0].strip()
        likes = (
            metadata.split('-')[0].split('likes, ')[0].replace(',', '').strip()
        )
        comments = (
            metadata.split('-')[0].split('likes, ')[1]
            .split('comment')[0].replace(',', '').strip()
        )
        author = metadata.split('- ')[1].split(' ')[0].strip()
        date = (
            ' '.join(metadata.split('- ')[1].split(' ')[2::])[:-1]
            .replace(',', '').strip()
        )

        yield {
            'likes': likes.replace('"', ''),
            'comments': comments.replace('"', ''),
            'author': author.replace('"', ''),
            'date': date.replace('"', ''),
            'description': ' '.join(description).split('"')[1]
                           .replace('\r', ' ').replace('\n', ' ')
                           .strip().replace('"', '')
        }
