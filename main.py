from views.views_generate import urls_views, close_connection
import telebot
import requests
import re

bot = telebot.TeleBot("2033192880:AAEBcU8OtU0AkVATJp_ak9LvGsWZCrh6zF0")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "🤓Genera vistas de forma automática en sitios de internet \n\n"
                          "❌Agrega una dirección de internet para generar views❌")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
#     print(message.text)
@bot.message_handler(func=lambda message: True)
def view_web(message):
    # Check url
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s(" \
            r")<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])) "
    url = re.match(regex, message.text)
    if url:
        # for item in list(message.text):
        urls_views(message.text, delay=5)
        bot.send_message(message.chat.id, "Finalizado")
        close_connection()
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
