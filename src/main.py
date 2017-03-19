# -*- coding: utf-8 -*-   
import telebot
import os

from weather import get_current_weather_in_location, is_bad_weather

# Creating the bot
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN') # Token previously stored in an environment var
bot = telebot.TeleBot(TOKEN)


# The decorator (@bot.message_handler) indicates the type of messages that will activate this function
@bot.message_handler(content_types=['location'])
def answer_if_I_have_to_worry_from_location_message(message):

    # Getting the current weather
    weathers = get_current_weather_in_location(message)

    # Checking if it's raining/snowing/thunderstorming/etc
    I_need_to_worry = [is_bad_weather(weather) for weather in weathers]


    if True in I_need_to_worry:
        bot.reply_to(message, 'Males notícies... Si tens roba estesa, ja cal que la llaves altra volta')
    else:
        bot.reply_to(message, 'Pots estar tranquil, que fa bon temps!')


@bot.message_handler(regexp='^ping$')
def test_that_bot_works(message):
    bot.reply_to(message, 'ACK')

# Starting the bot
bot.polling(none_stop=True)
