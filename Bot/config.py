import os


bot_token = '1776652361:AAEJWQC4X-NY8SXn2vDACsaAcKouJ7WkeG0'


#MONGODB_URI = 'mongodb+srv://WeatherBot:vCVaDVvEqRf6zZs@cluster0.xicxe.mongodb.net/WeatherBotDB?retryWrites=true&w=majority'

HEROKU_APP_NAME = 'bagirtelegramweatherbot'

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{bot_token}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT', 5000))