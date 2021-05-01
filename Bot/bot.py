from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import start_webhook

import config
import keyboards
import bs4_parse


bot = Bot(token=config.bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def on_startup(dp):
    await bot.set_webhook(config.WEBHOOK_URL, drop_pending_updates=True)


@dp.message_handler(commands=['catalog'])
async def catalog_command(message: types.Message):
    await message.answer(text='Каталог:', reply_markup=keyboards.main_keyboard())


@dp.callback_query_handler(text='back_button')
async def catalog_command(call: types.CallbackQuery):
    await call.message.answer(text='Каталог:', reply_markup=keyboards.main_keyboard())


@dp.callback_query_handler(text='catalog_button')
async def set_catalog_keyboard(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=keyboards.first_categories_keyboard())


@dp.callback_query_handler(text='laptops_and_accessories_button')
async def set_laptops_and_accessories_keyboard(call: types.CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=keyboards.laptos_and_accessories_keyboard())


@dp.callback_query_handler(text='laptops_button')
async def show_laptops(call: types.CallbackQuery):
    items = bs4_parse.items
    i = 0
    msg_text = items[i]['name'] + '\n' + items[i]['price']
    await bot.send_photo(chat_id=call.from_user.id, photo=items[i]['img'])
    await call.message.answer(text=msg_text, reply_markup=keyboards.item_keyboard())


if __name__ == '__main__':
    #executor.start_polling(dp, skip_updates=True)
    start_webhook(
        dispatcher=dp,
        webhook_path=config.WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=config.WEBAPP_HOST,
        port=config.WEBAPP_PORT
    )