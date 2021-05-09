import requests
import lxml
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import sys

url = 'https://matrix12.ru/'


def get_text(url):
    r = requests.get(url)
    text = r.text

    return text


text = get_text(url)
soup = BeautifulSoup(text, "html.parser")
goods_ul = soup.find('ul', {'class': 'goods_menu_wrap level_1 as-catalog-menu'})


def get_first_level_categories():
    goods_ul = soup.find('ul', {'class': 'goods_menu_wrap level_1 as-catalog-menu'})
    fl_categories = []
    first_level_categories = goods_ul.find_all('a', {'class': "goods_menu__link"}, href=True)
    for fl_category in first_level_categories:
        spans = fl_category.find_all('span')
        for span in spans:
            fl_categories.append({'text': span.text,
                                  'link': fl_category['href']})

    return fl_categories


def get_second_level_categories(fl_category):
    goods_ul = soup.find('ul', {'class': 'goods_menu_wrap level_1 as-catalog-menu'})
    sl_categories = []
    sl_categories_ul = goods_ul.findAll('ul', {'class': "level_2"})
    for category in sl_categories_ul:
        check_list = category.findAll('li', {'class': "title"})
        for check in check_list:
            if check.text == fl_category['text']:
                if category.findAll('li', {'class': 'subpages'}):
                    sl_categories_li = category.findAll('li', {'class': 'subpages'})
                    for sl_categories_a in sl_categories_li:
                        if not sl_categories_a.findParent('table'):
                            sl_category_a = sl_categories_a.findAll('a', href=True)
                            for sl_category in sl_category_a:
                                if not sl_category.findParent('table'):
                                    sl_categories.append({'text': sl_category.text,
                                                          'link': sl_category['href']})
                else:
                    sl_categories_a = category.findAll('a')
                    for sl_category in sl_categories_a:
                        sl_categories.append({'text': sl_category.text,
                                              'link': sl_category['href']})

    return sl_categories


def get_third_level_categories(sl_category):
    goods_ul = soup.find('ul', {'class': 'goods_menu_wrap level_1 as-catalog-menu'})
    tl_categories = []
    tl_categories_li = goods_ul.find_all('li', {'class': "subpages"})
    for tl_categories_table_block in tl_categories_li:
        tl_category_a = tl_categories_table_block.find('a')
        if tl_category_a.text == sl_category['text']:
            tl_category_table = tl_categories_table_block.findAll('ul')
            for tl_categories_table in tl_category_table:
                tl_categories_rows = tl_categories_table.findAll('a', href=True)
                for tl_category in tl_categories_rows:
                    tl_categories.append({'text': tl_category.text,
                                          'link': tl_category['href']})

    return tl_categories



site = 'https://matrix12.ru'
for_img = 'https://matrix12.ru'


def get_items(category):
    items = []
    site = 'https://matrix12.ru'
    link = category['link']
    url = site + link
    soup = BeautifulSoup(urlopen(url), "html.parser")
    li = soup.find_all('li', {'class': 'catalog_wrap_item_a'})
    for l in li:
        name = l.find('div', {'class': "catalog_item_info"})
        price = l.find('span', {'class': "editor-pane-num"})
        img = l.find('img')
        item = {'name': re.sub(' +', ' ', re.sub('\n', ' ', name.text)),
                'price': re.sub(' +', ' ', re.sub('\n', ' ', price.text.replace("*", ""))), 'img': site + img['src']}
        items.append(item)
    print(items)
    return items

