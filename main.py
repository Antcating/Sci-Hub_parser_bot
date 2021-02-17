# =============================================================================
# Sci-HUB parser
# =============================================================================
import telebot, os
from time import sleep
from telebot import types as tp
import requests 
import bs4 

try:
    bot_input = open("bot_token.tg", 'r').read()
except:
    bot_input = input('Incert Bot Token here: ')
    bot_token_write = open('bot_token.tg','w+')
    bot_token_write.write(bot_input)
    bot_token_write.close()
bot = telebot.TeleBot(bot_input)

main_menu = tp.ReplyKeyboardMarkup(one_time_keyboard=True)  # create selection keyboard
main_menu.add('📖 Get document')


@bot.message_handler(commands=['start', 'menu', 'help'])
def help_message(message):
    bot.send_message(message.from_user.id, 'Main Menu',reply_markup=main_menu)
    
@bot.message_handler(content_types=['text'])
def bot_input(message):
    if message.text == '📖 Get document':
        bot.send_message(message.from_user.id, 'Input DOI entry')
        bot.register_next_step_handler(message, sci_hub)


def sci_hub(message):

    doi_str = message.text
    url = 'https://sci-hub.do/' + doi_str
    r = requests.get(url, stream=True)
    print(r.text.startswith('<!DOCTYPE html>'))
    if r.text.startswith('<!DOCTYPE html>') == False:
        bot.send_message(message.from_user.id, 'There is no article with this DOI!')
        return
    else:
        soup = bs4.BeautifulSoup(r.text, "html.parser") 
        div = str(soup.find('iframe', id="pdf").extract()).split('"')[3]
        div_url = requests.get(div, stream=True)       
        bot.send_document(message.from_user.id,div_url.content)

if __name__ == '__main__':
    while True:
        try:
            bot.infinity_polling(True)
        except KeyboardInterrupt:
            on = 0
            print("Exiting the program")
            os.abort()
        except:
            print("No access to telegram")
            sleep(15)