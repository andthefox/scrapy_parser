import scrapy
from urllib.parse import urljoin


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """
        Собирает ссылки на документы PEP
        """
        all_peps = response.css(
            '#numerical-index > h2 + table > tbody > '
            'tr > td:nth-child(2) > a::attr(href)'
        ).extract()
        for pep_link in all_peps:
            pep_link = urljoin(
                self.start_urls[0],
                pep_link
            )
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """
        Парсит страницы с документами, формирует Items
        """
        pep_number = response.css(
            'li:contains("PEP Index") + li::text'
        ).get().replace('PEP ', '').strip()
        pep_header = ' '.join(response.css(
            '#pep-content > h1::text'
        ).getall()).split('–')[1].strip().strip('\"')
        yield {
            'number': int(pep_number),
            'name': pep_header.strip(),
            'status': response.css(
                'dt:contains("Status") + dd *::text'
            ).get()
        }
