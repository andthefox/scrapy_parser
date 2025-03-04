# scrapy_parser_pep

Проект парсинга рилсов с использованием Scrapy.

## Что может приложение?
- Выводит список описаний рилсов

### Установка
1. Клонировать репозиторий:
```
git clone git@github.com:andthefox/scrapy_parser.git

git checkout reels_description
```
1. 1. Альтернативный вариант: запустить `start.bat`. Установка и запуск произойдет автоматически.
2. Создать виртуальное окружение:
```
python3 -m venv venv
```
3. Активировать вирутальное окружение:
```
source venv/bin/activate
```
4. Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
5. Перейти в корневую папку проекта
```
cd ../
```

### Использование

- Вставить ссылки на рилсы в файл list.csv в корне проекта. Каждая ссылка должна быть на новой строке.

- Запустить парсер:

```
scrapy crawl insta
```

Парсер создает папку results с выходными данными парсинга.
В файле "insta_reels_ДатаВремя.csv" содержится список рилсов с информацией об авторах, описанием, дате публикации и количеством лайков и комментов.

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
