# -*- coding: utf-8 -*-   

import random

import telebot
import os
from flask import Flask, request

from weather import get_current_weather_in_location

# Creating the bot
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN') # Token previously stored in an environment var
bot = telebot.TeleBot(TOKEN)

# Creating the server
server = Flask(__name__)


# The decorator (@bot.message_handler) indicates the type of messages that will activate this function
@bot.message_handler(content_types=['location'])
def get_current_weather_from_location_message(message):
    weather = get_current_weather_in_location(message)
    bot.reply_to(message, weather)

@bot.message_handler(regexp='^ping$')
def test_that_bot_works(message):
    bot.reply_to(message, 'ACK')

# Server configuration
@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://maltiempobot.herokuapp.com/bot")
    return "!", 200

# Running the server
# It's very important to set the port with the environment variable, because it's how heroku stores it
server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = Flask(__name__)
