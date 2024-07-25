# scrapy_parser_pep

Проект парсинга PEP с использованием Scrapy.

## Что может приложение?
- Выводит список PEP (Python Enhancement Proposals), их названия, номера и статус
- Выводит данные о количестве PEP в том или ином статусе

### Установка
1. Клонировать репозиторий:
```
git clone git@github.com:arhstd/scrapy_parser_pep.git
```
2. Перейти в папку в командной строке:
```
cd scrapy_parser_pep
```
3. Создать виртуальное окружение:
```
python3 -m venv venv
```
4. Активировать вирутальное окружение:
```
source venv/bin/activate
```
5. Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
6. Перейти в папку с исходным кодом в командной строке:
```
cd src
```

### Использование
```
scrapy crawl pep
```

Парсер создает папку results с выходными данными парсинга.
В файле "pep_ДатаВремя.csv" содержится список PEP с номерами, названиями и статусами.
В файле "status_summary_ДатаВремя.csv" содержится количество PEP в определенных статусах и их суммарное число.

### Стек использованных технологий
* Python, список дополнительных пакетов:
    * attrs
    * Automat
    * cffi
    * constantly
    * cryptography
    * cssselect
    * flake8
    * h2
    * hpack
    * hyperframe
    * hyperlink
    * idna
    * importlib-metadata
    * incremental
    * iniconfig
    * itemadapter
    * itemloaders
    * jmespath
    * lxml
    * mccabe
    * packaging
    * parsel
    * pluggy
    * priority
    * Protego
    * py
    * pyasn1
    * pyasn1-modules
    * pycodestyle
    * pycparser
    * PyDispatcher
    * pyflakes
    * pyOpenSSL
    * pyparsing
    * pytest
    * pytest-pythonpath
    * queuelib
    * Scrapy
    * service-identity
    * six
    * toml
    * Twisted
    * typing_extensions
    * w3lib
    * zipp
    * zope.interface

> Автор: Шевкунов А. ([arhstd](https://github.com/arhstd))
