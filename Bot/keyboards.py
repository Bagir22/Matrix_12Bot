from aiogram import types


def main_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard_catalog = types.InlineKeyboardButton(text="Каталог", callback_data="catalog_button")
    keyboard.add(keyboard_catalog)

    return keyboard


def first_categories_keyboard(fl_categories):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for fl_category in fl_categories:
        keyboard.insert(
            types.InlineKeyboardButton(text=f'{fl_category["text"]}', callback_data=f"{fl_categories.index(fl_category)}_fc_btn"))
    keyboard_back = types.InlineKeyboardButton(text="Назад", callback_data="back_button")
    keyboard.add(keyboard_back)

    return keyboard


def second_categories_keyboard(sl_categories):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for sl_category in sl_categories:
        keyboard.insert(
            types.InlineKeyboardButton(text=f'{sl_category["text"]}', callback_data=f"{sl_categories.index(sl_category)}_sc_btn"))
    keyboard_back = types.InlineKeyboardButton(text="Назад", callback_data="back_button")
    keyboard.add(keyboard_back)

    return keyboard


def third_categories_keyboard(tl_categories):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for tl_category in tl_categories:
        keyboard.insert(
            types.InlineKeyboardButton(text=f'{tl_category["text"]}', callback_data=f'{tl_categories.index(tl_category)}_tc_btn'))
    keyboard_back = types.InlineKeyboardButton(text="Назад", callback_data="back_button")
    keyboard.add(keyboard_back)

    return keyboard


def item_keyboard(items):
    keyboard = types.InlineKeyboardMarkup()
    if len(items) > 1:
        keyboard_previous = types.InlineKeyboardButton(text="<<", callback_data="previous_button")
        keyboard_next = types.InlineKeyboardButton(text=">>", callback_data="next_button")
        keyboard.add(keyboard_previous, keyboard_next)
    keyboard_back = types.InlineKeyboardButton(text="Назад", callback_data="back_button")
    keyboard.row(keyboard_back)

    return keyboard

