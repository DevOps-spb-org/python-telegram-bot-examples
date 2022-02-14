from dotenv import load_dotenv
import os
import telebot
import random
from telebot import types

f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()

load_dotenv()

BOT_KEY = os.getenv('BOT_KEY')

bot = telebot.TeleBot(BOT_KEY)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Факт")
    item2 = types.KeyboardButton("Поговорка")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id,
                     'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',
                     reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    elif message.text.strip() == 'Поговорка':
        answer = random.choice(thinks)
    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True, interval=0)
