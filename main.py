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
    #Check url

    #for item in list(message.text):
    urls_views(message.text, delay=5)
    bot.send_message(message.chat.id,"Finalizado")
    close_connection()

bot.infinity_polling()

# urls = [
#     "https://notiremedios.com/QXpa"
#     , "https://notiremedios.com/Jk8UGgCK"
#     , "https://notiremedios.com/Ammeg"
#     , "https://notiremedios.com/uCqm"
#     , "https://notiremedios.com/5XLWiA"
# ]
#
# for item in urls:
#     urls_views(item, delay=5)
# print("Finished all conections close the webbrowser object !!! ")
# close_connection()
