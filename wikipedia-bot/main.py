from dotenv import load_dotenv
import os
import telebot
import wikipedia
import re

load_dotenv()

BOT_KEY = os.getenv('BOT_KEY')

bot = telebot.TeleBot(BOT_KEY)

wikipedia.set_lang('ru')


def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''

        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break

        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2
    except Exception as e:
        return 'Нет такой информации'


@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


bot.polling(none_stop=True, interval=0)
