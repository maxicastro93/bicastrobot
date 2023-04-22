from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import time
import os

# Configura tu token y chat_id de Telegram como variables de entorno
BOT_TOKEN = os.environ.get('5851311227:AAEZCgzvjmv0F8btce0X7v1zI8xAO0L4oq4')
CHAT_ID = os.environ.get('bicastroBot')

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(url, data=data)
    return response.json()

if __name__ == '__main__':
    while True:
        if check_website('https://www.example.com'):
            send_telegram_message('La web está en funcionamiento')
        else:
            send_telegram_message('La web no está en funcionamiento')

        # Espera 1 hora antes de volver a comprobar la web
        time.sleep(3600)
