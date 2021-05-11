from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import start_webhook


import config
import keyboards
import bs4_parse
import mongodb


import re


bot = Bot(token=config.bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def on_startup(dp):
    await bot.set_webhook(config.WEBHOOK_URL, drop_pending_updates=True)


@dp.message_handler(commands=['start'])
@dp.message_handler(commands=['catalog'])
async def catalog_command(message: types.Message):
    mongodb.insert_data_into_db(id=message.chat.id)
    await message.answer(text='Каталог:', reply_markup=keyboards.main_keyboard())


@dp.callback_query_handler(text='back_button')
async def catalog_command(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='Каталог:', reply_markup=keyboards.main_keyboard())


@dp.callback_query_handler(text='catalog_button')
async def set_fl_catalog_keyboard(call: types.CallbackQuery):
    fl_categories = bs4_parse.get_first_level_categories()
    await call.message.edit_reply_markup(reply_markup=keyboards.first_categories_keyboard(fl_categories))


@dp.callback_query_handler(text_contains='_fc_btn')
async def set_sl_catalog_keyboard(call: types.CallbackQuery):
    id = call.message.chat.id
    fl_category_index = re.findall(r'[0-9]+', call.data)
    fl_categories = bs4_parse.get_first_level_categories()
    fl_category = fl_categories[int(fl_category_index[0])]
    sl_categories = bs4_parse.get_second_level_categories(fl_category)
    mongodb.insert_fl_categories(id, fl_categories, fl_category, sl_categories)
    if not sl_categories:
        items = bs4_parse.get_items(category=fl_category)
        i = 0
        mongodb.update_items(id, items, i, category=fl_category['text'])
        await call.message.answer_photo(photo=items[i]['img'],
                                        caption=f"Категория: {fl_category['text']}\n"
                                                f"{items[i]['name']}\n "
                                                f"Цена: {items[i]['price']}",
                                        reply_markup=keyboards.item_keyboard())
    else:
        await call.message.edit_reply_markup(reply_markup=keyboards.second_categories_keyboard(sl_categories))


@dp.callback_query_handler(text_contains='_sc_btn')
async def set_tl_catalog_keyboard(call: types.CallbackQuery):
    id = call.message.chat.id
    sl_categories, fl_category = mongodb.get_sls_fl(id)
    sl_category_index = re.findall(r'[0-9]+', call.data)
    sl_category = sl_categories[int(sl_category_index[0])]
    tl_categories = bs4_parse.get_third_level_categories(sl_category)
    mongodb.insert_tl_categories(id, sl_category, tl_categories)
    if not tl_categories:
        items = bs4_parse.get_items(category=sl_category)
        i = 0
        mongodb.update_items(id, items, i, category=sl_category['text'])
        await call.message.answer_photo(photo=items[i]['img'],
                                        caption=f"Категория: {sl_category['text']}\n"
                                                f"{items[i]['name']}\n "
                                                f"Цена: {items[i]['price']}",
                                        reply_markup=keyboards.item_keyboard())
    else:
        await call.message.edit_reply_markup(reply_markup=keyboards.third_categories_keyboard(tl_categories))


@dp.callback_query_handler(text_contains='_tc_btn')
async def items_button(call: types.CallbackQuery):
    id = call.message.chat.id
    tl_categories = mongodb.get_tls(id)
    tl_category_index = re.findall(r'[0-9]+', call.data)
    tl_category = tl_categories[int(tl_category_index[0])]
    items = bs4_parse.get_items(category=tl_category)
    i = 0
    mongodb.update_items(id, items, i, category=tl_category['text'])
    await call.message.answer_photo(photo=items[i]['img'],
                                    caption=f"Категория: {tl_category['text']}\n"
                                            f"{items[i]['name']}\n "
                                            f"Цена: {items[i]['price']}",
                                    reply_markup=keyboards.item_keyboard())


@dp.callback_query_handler(text='next_button')
@dp.callback_query_handler(text='previous_button')
async def next_button(call: types.CallbackQuery):
    id = call.message.chat.id
    items, i, category = mongodb.get_items(id)
    if call.data == 'next_button':
        i += 1
    else:
        i -= 1

    mongodb.update_items(id, items, i, category)
    await call.message.delete()
    await call.message.answer_photo(photo=items[i]['img'],
                                    caption=f"Категория: {category}\n"
                                            f"{items[i]['name']}\n "
                                            f"Цена: {items[i]['price']}",
                                    reply_markup=keyboards.item_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    '''
    start_webhook(
        dispatcher=dp,
        webhook_path=config.WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=config.WEBAPP_HOST,
        port=config.WEBAPP_PORT
    )
    '''






