from aiogram import types


def main_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard_catalog = types.InlineKeyboardButton(text="Каталог", callback_data="catalog_button")
    keyboard_back = types.InlineKeyboardButton(text="Назад", callback_data="main_back_button")
    keyboard.add(keyboard_catalog, keyboard_back)

    return keyboard


def first_categories_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    keyboard_appliances_btn = types.InlineKeyboardButton(text="Бытовая техника", callback_data="appliances_button")
    keyboard_laptops_and_accessories_btn = types.InlineKeyboardButton(text="Ноутбуки и аксессуары", callback_data="laptops_and_accessories_button")
    keyboard_computers_and_accessories_btn = types.InlineKeyboardButton(text="Компьютеры и комплектующие", callback_data="computers_and_accessories_button")
    keyboard_peripherals_btn = types.InlineKeyboardButton(text="Периферийные устройства", callback_data="peripherals_button")
    keyboard_portable_btn = types.InlineKeyboardButton(text="Портативная техника", callback_data="portable_button")
    keyboard_phones_and_accessories_btn = types.InlineKeyboardButton(text="Телефоны и аксессуары", callback_data="phones_and_accessories_button")
    keyboard_tablets_and_accessories_btn = types.InlineKeyboardButton(text="Планшеты и аксессуары", callback_data="tablets_and_accessories_button")
    keyboard_photo_and_video_btn = types.InlineKeyboardButton(text="Фото и видео", callback_data="photo_and_video_button")
    keyboard_office_equipment_btn = types.InlineKeyboardButton(text="Печатная и офисная техника, канцтовары", callback_data="office_equipment_button")
    keyboard_tele_audio_btn = types.InlineKeyboardButton(text="Теле-Аудио-Видео техника", callback_data="tele_audio_button")
    keyboard_network_btn = types.InlineKeyboardButton(text="Сетевое оборудование", callback_data="network_button")
    keyboard_automotive_btn = types.InlineKeyboardButton(text="Автомобильная техника", callback_data="automotive_button")
    keyboard_external_storage_btn = types.InlineKeyboardButton(text="Внешние носители информации", callback_data="external_storage_button")
    keyboard_cabels_btn = types.InlineKeyboardButton(text="Кабели", callback_data="cabels_button")
    keyboard_games_btn = types.InlineKeyboardButton(text="Игры, софт, подписки", callback_data="games_button")
    keyboard_lighting_btn = types.InlineKeyboardButton(text="Освещение", callback_data="lighting_button")
    keyboard_comp_furniture_btn = types.InlineKeyboardButton(text="Компьютерная мебель", callback_data="comp_furniture_button")
    keyboard_kids_toys_btn = types.InlineKeyboardButton(text="Детские игрушки", callback_data="kids_toys_button")
    keyboard_activities = types.InlineKeyboardButton(text="Активный отдых и спорт", callback_data="activities_button")
    keyboard_services_btn = types.InlineKeyboardButton(text="Услуги", callback_data="services_button")
    keyboard_chemicals_btn = types.InlineKeyboardButton(text="Бытовая химия", callback_data="chemicals_button")
    keyboard_masks_btn = types.InlineKeyboardButton(text="Маски дизайнерские", callback_data="masks_button")
    keyboard_SIM_btn = types.InlineKeyboardButton(text="Сим-карты", callback_data="SIM_button")
    keyboard_commerce_btn = types.InlineKeyboardButton(text="Торгово-кассовое оборудование", callback_data="commerce_button")
    keyboard_certificates_btn = types.InlineKeyboardButton(text="Подарочные сертификаты", callback_data="certificates_button")
    keyboard_back = types.InlineKeyboardButton(text="Назад", callback_data="back_button")

    keyboard.add(keyboard_appliances_btn, keyboard_laptops_and_accessories_btn, keyboard_computers_and_accessories_btn,
                 keyboard_peripherals_btn, keyboard_portable_btn, keyboard_phones_and_accessories_btn, keyboard_tablets_and_accessories_btn,
                 keyboard_photo_and_video_btn, keyboard_office_equipment_btn, keyboard_tele_audio_btn, keyboard_network_btn,
                 keyboard_automotive_btn, keyboard_external_storage_btn, keyboard_cabels_btn, keyboard_games_btn, keyboard_lighting_btn, keyboard_comp_furniture_btn,
                 keyboard_kids_toys_btn, keyboard_activities, keyboard_services_btn, keyboard_chemicals_btn, keyboard_masks_btn, keyboard_SIM_btn, keyboard_commerce_btn,
                 keyboard_certificates_btn, keyboard_back)

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