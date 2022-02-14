from dotenv import load_dotenv
import os
import telebot
import time

load_dotenv()

BOT_KEY = os.getenv('BOT_KEY')
CHANNEL_NAME = os.getenv('CHANNEL_NAME')

bot = telebot.TeleBot(BOT_KEY)

f = open('data/fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    time.sleep(3600)
bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")
