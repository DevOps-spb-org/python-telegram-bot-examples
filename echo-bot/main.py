from dotenv import load_dotenv
import os
import telebot

load_dotenv()

BOT_KEY = os.getenv('BOT_KEY')

bot = telebot.TeleBot(BOT_KEY)


@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'I am online!')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


bot.polling(none_stop=True, interval=0)
