import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


url = 'https://matrix12.ru/'


second_level_categories_list = []
third_level_categories_list = []


def get_text(url):
    r = requests.get(url)
    text = r.text

    return text


text = get_text(url)


def get_first_level_categories(text):
    first_level_categories_list = []
    soup = BeautifulSoup(text, "html.parser")
    first_level_categories = soup.find_all('a', {'class': "goods_menu__link"})
    for categories in first_level_categories:
        spans = categories.find_all('span')
        for span in spans:
            first_level_categories_list.append(span.text)

    return first_level_categories_list


categories = get_first_level_categories(text)


site = 'https://matrix12.ru/goods/notebook/notebook/'
for_img = 'https://matrix12.ru'


def get_items(site):
    items = []
    soup = BeautifulSoup(urlopen(site), "html.parser")
    li = soup.find_all('li', {'class': 'catalog_wrap_item_a'})
    for l in li:
        name = l.find('div', {'class': "catalog_item_info"})
        price = l.find('span', {'class': "editor-pane-num"})
        img = l.find('img')
        item = {'name': re.sub(' +', ' ', re.sub('\n', ' ', name.text)),
                'price': re.sub(' +', ' ',  re.sub('\n', ' ', price.text.replace("*", ""))),
                'img': for_img + img['src']}
        items.append(item)
    return items


items = get_items(site)

