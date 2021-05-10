import os


bot_token = os.environ.get('bot_token')


MONGODB_URI = 'mongodb+srv://WeatherBot:vCVaDVvEqRf6zZs@cluster0.xicxe.mongodb.net/Matrix_12BotDB?retryWrites=true&w=majority'


HEROKU_APP_NAME = 'matrix12bot'

# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{bot_token}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT', 5000))