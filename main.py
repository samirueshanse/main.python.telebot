import os
import telebot

bot = telebot.TeleBot("5192610556:AAGtsM8SnfwAqOUvpKVwY8kwgie8SSipJ_E")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello! I am Chat BOT")

@bot.message_handler(commands=["how"])
def send_welcome(message):
    bot.reply_to(message,"https://t.me/Anytime_Sri_Lankan_link_Share")

@bot.message_handler(commands=["newpost"])
def send_welcome(message):
    bot.reply_to(message, " Goto the https://t.me/Inlinebuttons_bot 

@bot.message_handler(commands=["python"])
def send_welcome(message):
    bot.reply_to(message, "https://www.python.org/downloads/")

@bot.message_handler(commands=["beautiful"])
def send_welcome(message):
    bot.reply_to(message, "https://images.app.goo.gl/rCSgWPTJvH6yQ9k7A")

bot.polling()
