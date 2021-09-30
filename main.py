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


# Handling a list of web sites
@bot.message_handler(commands=['list'])
def handle_list(message):
    cleaned_ = message.text.replace('/list', '')
    url_list = list(cleaned_.split(","))
    print(url_list)


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


# Handler url and visit
@bot.message_handler(func=lambda message: True)
def view_web(message):
    # Check url
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, message.text) is not None:
        try:
            urls_views(message.text, delay=5)
            bot.send_message(message.chat.id, "Conexión exitosa")
            # close_connection()
        except Exception as ex:
            bot.send_message(message.chat.id, f"Se produjo un error al conectarse a la página {ex}")

    else:
        bot.send_message(message.chat.id, " Error !!! \n Inserte direcciones de internet correctas !!!")


bot.infinity_polling()

# urls = [
#     "https://notiremedios.com/QXpa"
#     , "https://notiremedios.com/Jk8UGgCK"
#     , "https://notiremedios.com/Ammeg"
#     , "https://notiremedios.com/uCqm"
#     , "https://notiremedios.com/5XLWiA"
# ]
#
