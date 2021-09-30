import requests
import re
import telebot
from views.views_generate import urls_views, close_connection
from info import info

# CONSTANTS
INFO = info
N_VIEWS = 0
bot = telebot.TeleBot("2033192880:AAEBcU8OtU0AkVATJp_ak9LvGsWZCrh6zF0")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, INFO)


@bot.message_handler(commands=['vista'])
def n_views(message):
    global N_VIEWS
    N_VIEWS = int(message.text.replace('/vista', ''))
    bot.send_message(message.chat.id, f"Se va visitar {N_VIEWS} veces cada pagina")
# Handling a list of web sites
@bot.message_handler(commands=['list'])
def handle_list(message):
    output = []
    cleaned_ = message.text.replace('/list', '')
    url_tmp = list(cleaned_.split(","))
    url_list = list(map(lambda f: f.replace(' ', ''), url_tmp))

    print(f"La lista de direciones es --> {url_list}")
    for item in url_list:
        try:
            output.append(urls_views(item, 5, N_VIEWS))
        except Exception as e:
            print(f"Se produjo un error con la web \n {item} --> {e}")
    bot.send_message(message.chat.id, f" {output}")


# Setting views to visit web pages
@bot.message_handler(commands=['nviews'])
def set_views(message):
    int_message = int(message.text.replace('/nviews', ''))
    if int_message != 0:
        if int_message <= 1000:
            global N_VIEWS
            N_VIEWS = int_message
            bot.send_message(message.chat.id, f"{int_message}")
            print(f"cantidad de views --> {int_message}")
        else:
            bot.send_message(message.chat.id, "cantidad de views diarios no pueden ser mayor que --> 1000")
            print("cantidad de views diarios no pueden ser mayor que --> 1000")
    else:
        bot.send_message(message.chat.id, "-")


bot.infinity_polling()

# urls = [
#     "https://notiremedios.com/QXpa"
#     , "https://notiremedios.com/Jk8UGgCK"
#     , "https://notiremedios.com/Ammeg"
#     , "https://notiremedios.com/uCqm"
#     , "https://notiremedios.com/5XLWiA"
# ]
#
