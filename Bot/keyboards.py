from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.parts import paginate
from bs4_parse import categories


def main_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard_catalog = types.InlineKeyboardButton(text="Каталог", callback_data="catalog_button")
    keyboard_back = types.InlineKeyboardButton(text="Назад", callback_data="main_back_button")
    keyboard.add(keyboard_catalog, keyboard_back)

    return keyboard


def first_categories_keyboard(*args):
    keyboard = types.InlineKeyboardMarkup()
    for category in categories:
        keyboard.insert(
            types.InlineKeyboardButton(text=f'{category}', callback_data=f"{categories.index(category)}_fc_btn"))
    keyboard_back = types.InlineKeyboardButton(text="Назад", callback_data="back_button")
    keyboard.add(keyboard_back)
    return keyboard

def laptos_and_accessories_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard_laptops_btn = types.InlineKeyboardButton(text="Ноутбуки", callback_data="laptops_button")
    keyboard_laptop_batteries_btn = types.InlineKeyboardButton(text="Аккумуляторы к ноутбукам", callback_data="laptop_batteries_button")
    keyboard_power_supplies_orig_btn = types.InlineKeyboardButton(text="Блоки питания к ноутбукам оригинальные", callback_data="power_supplies_orig_button")
    keyboard_power_supplies_univ_btn = types.InlineKeyboardButton(text="Блоки питания к ноутбукам универсальные", callback_data="power_supplies_univ_button")
    keyboard_laptop_keyboard_btn = types.InlineKeyboardButton(text="Клавиатуры ддля ноутбуков", callback_data="laptop_keyboards_button")
    keyboard_laptop_matrices_btn = types.InlineKeyboardButton(text="Матрицы для ноутбуков", callback_data="laptop_matrices_button")
    keyboard_laptop_stands_btn = types.InlineKeyboardButton(text="Охлаждающие подставки", callback_data="laptop_stands_button")
    keyboard_backpacks_btn = types.InlineKeyboardButton(text="Рюкзаки", callback_data="backpacks_button")
    keyboard_laptop_handbags_btn = types.InlineKeyboardButton(text="Сумки для ноутбуков", callback_data="laptop_handbags_button")
    keyboard_back = types.InlineKeyboardButton(text="Назад", callback_data="back_button")
    keyboard.add(keyboard_laptops_btn,keyboard_laptop_batteries_btn, keyboard_power_supplies_orig_btn, keyboard_power_supplies_univ_btn, keyboard_laptop_keyboard_btn,
                 keyboard_laptop_matrices_btn, keyboard_laptop_stands_btn, keyboard_backpacks_btn, keyboard_laptop_handbags_btn, keyboard_back)
    return keyboard


def item_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard_previous = types.InlineKeyboardButton(text="<<", callback_data="previous_button")
    keyboard_next = types.InlineKeyboardButton(text=">>", callback_data="next_button")
    keyboard_back = types.InlineKeyboardButton(text="Назад", callback_data="back_button")
    keyboard.add(keyboard_previous, keyboard_next)
    keyboard.row(keyboard_back)
    return keyboard

