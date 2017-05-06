# -*- coding: utf-8 -*-   
import os
import telebot

from constants import TODAY_WORRY_VAL, TODAY_WORRY_ENG, TODAY_NO_WORRY_VAL, TODAY_NO_WORRY_ENG, FORECAST_WORRY_VAL, \
    FORECAST_WORRY_ENG, FORECAST_NO_WORRY_ENG, FORECAST_NO_WORRY_VAL, LOCATION_STORED_CORRECTLY_ENG, \
    LOCATION_STORED_CORRECTLY_VAL, LOCATION_NOT_STORED_CORRECTLY_ENG, LOCATION_NOT_STORED_CORRECTLY_VAL, HELP_VAL, \
    HELP_ENG
from utils import store_user_location, get_user_location, ask_user_location, is_bot_English
from weather import is_bad_weather, get_5day_forecast_in_location, \
    get_today_forecast_in_location

# Creating the bot
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN') # Token previously stored in an environment var
bot = telebot.TeleBot(TOKEN)


# The decorator (@bot.message_handler) indicates the type of messages that will activate this function
@bot.message_handler(commands=['paraguas', 'umbrella'])
def answer_if_I_have_to_worry_from(message):

    # Getting the current weather
    lat, lon = get_user_location(message.from_user)
    weathers = get_today_forecast_in_location(lat, lon)

    # Not checking the weather if we don't have user's location
    if not weathers:
        ask_user_location(bot, message)
        return None

    # Checking if it's raining/snowing/thunderstorming/etc
    I_need_to_worry = [is_bad_weather(weather) for weather in weathers]

    # Answering to the user
    if True in I_need_to_worry:
        answer = TODAY_WORRY_ENG if is_bot_English() else TODAY_WORRY_VAL
        bot.reply_to(message, answer)
    else:
        answer = TODAY_NO_WORRY_ENG if is_bot_English() else TODAY_NO_WORRY_VAL
        bot.reply_to(message, answer)


@bot.message_handler(commands=['lavadora', 'washingmachine'])
def check_5day_forecast(message):
    """Method that indicates if there will be any bad weather in the following 5 days"""

    lat, lon = get_user_location(message.from_user)
    weathers = get_5day_forecast_in_location(lat, lon)

    # Not checking the weather if we don't have user's location
    if not weathers:
        ask_user_location(bot, message)
        return None

    # Checking if it's raining/snowing/thunderstorming/etc
    I_need_to_worry = [is_bad_weather(weather) for weather in weathers]

    if True in I_need_to_worry:
        answer = FORECAST_WORRY_ENG if is_bot_English() else FORECAST_WORRY_VAL
        bot.reply_to(message, answer)
    else:
        answer = FORECAST_NO_WORRY_ENG if is_bot_English() else FORECAST_NO_WORRY_VAL
        bot.reply_to(message, answer)


@bot.message_handler(content_types=['location'])
def update_user_location(message):
    """Saves or updates the location for the current user"""
    location_stored_correctly = store_user_location(message.from_user, message.location)

    if location_stored_correctly:
        answer = LOCATION_STORED_CORRECTLY_ENG if is_bot_English() else LOCATION_STORED_CORRECTLY_VAL
        bot.reply_to(message, answer)
    else:
        answer = LOCATION_NOT_STORED_CORRECTLY_ENG if is_bot_English() else LOCATION_NOT_STORED_CORRECTLY_VAL
        bot.reply_to(message, answer)


@bot.message_handler(commands=['start', 'help'])
def get_commands_help(message):
    """Shows a list of all the current commands"""
    response = HELP_ENG if is_bot_English() else HELP_VAL
    bot.reply_to(message, response)


@bot.message_handler(regexp='^ping$')
def test_that_bot_works(message):
    bot.reply_to(message, 'ACK')

# Starting the bot
bot.polling(none_stop=True)
