# -*- coding: utf-8 -*-   
import os
import telebot
from telebot import types

from constants import TODAY_WORRY_VAL, TODAY_WORRY_ENG, TODAY_NO_WORRY_VAL, TODAY_NO_WORRY_ENG, FORECAST_WORRY_VAL, \
    FORECAST_WORRY_ENG, FORECAST_NO_WORRY_ENG, FORECAST_NO_WORRY_VAL, LOCATION_STORED_CORRECTLY_ENG, \
    LOCATION_STORED_CORRECTLY_VAL, LOCATION_NOT_STORED_CORRECTLY_ENG, LOCATION_NOT_STORED_CORRECTLY_VAL, HELP_VAL, \
    HELP_ENG, INTRODUCTION_ENG, INTRODUCTION_VAL, LOW_TEMPERATURE_ENG, LOW_TEMPERATURE_VAL
from utils import store_user_location, get_user_location, ask_user_location, is_bot_English
from weather import is_bad_weather, get_3day_forecast_in_location, \
    get_today_forecast_in_location, get_today_temperatures_in_location

# Creating the bot
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')  # Token previously stored in an environment var
bot = telebot.TeleBot(TOKEN)


# The decorator (@bot.message_handler) indicates the type of messages that will activate this function
@bot.message_handler(commands=['paraguas', 'umbrella'])
def umbrella(message):

    # Getting the current weather
    lat, lon = get_user_location(message.from_user)
    forecast = get_today_forecast_in_location(lat, lon)

    # Not checking the weather if we don't have user's location
    if not forecast:
        ask_user_location(bot, message)
        return None

    # Checking if it's raining/snowing/thunderstorming/etc
    i_need_to_worry = forecast.is_bad()

    # Answering to the user
    if True in i_need_to_worry:
        answer = TODAY_WORRY_ENG if is_bot_English() else TODAY_WORRY_VAL
    else:
        answer = TODAY_NO_WORRY_ENG if is_bot_English() else TODAY_NO_WORRY_VAL
    bot.reply_to(message, answer)


@bot.message_handler(commands=['frio', 'cold'])
def cold(message):
    """Method that indicates the lowest temperature of the following 24 hours"""

    lat, lon = get_user_location(message.from_user)

    # Not checking the weather if we don't have user's location
    if (lat == -1) and (lon == -1):
        ask_user_location(bot, message)
        return None
    # If we have it, we'll get the min temperature and answering the user
    else:
        temperatures = get_today_temperatures_in_location(lat, lon)
    min_temperature = min(temperatures)

    # Answering to the user
    if is_bot_English():
        answer = LOW_TEMPERATURE_ENG.format(min_temperature)
    else:
        answer = LOW_TEMPERATURE_VAL.format(min_temperature)
    bot.reply_to(message, answer)


@bot.message_handler(commands=['lavadora', 'washingmachine'])
def washingmachine(message):
    """Method that indicates if there will be any bad weather in the following 3 days"""

    lat, lon = get_user_location(message.from_user)
    forecast = get_3day_forecast_in_location(lat, lon)

    # Not checking the weather if we don't have user's location
    if not forecast:
        ask_user_location(bot, message)
        return None

    # Checking if it's raining/snowing/thunderstorming/etc
    i_need_to_worry = forecast.is_bad()

    # Choosing the language and answering the user
    if True in i_need_to_worry:
        answer = FORECAST_WORRY_ENG if is_bot_English() else FORECAST_WORRY_VAL
    else:
        answer = FORECAST_NO_WORRY_ENG if is_bot_English() else FORECAST_NO_WORRY_VAL
    bot.reply_to(message, answer)


@bot.message_handler(content_types=['location'])
def update_user_location(message):
    """Saves or updates the location for the current user"""
    location_stored_correctly = store_user_location(message.from_user, message.location)

    if location_stored_correctly:
        answer = LOCATION_STORED_CORRECTLY_ENG if is_bot_English() else LOCATION_STORED_CORRECTLY_VAL
    else:
        answer = LOCATION_NOT_STORED_CORRECTLY_ENG if is_bot_English() else LOCATION_NOT_STORED_CORRECTLY_VAL

    # Creating a custom keyboard to simplify the commands entering process
    keyboard = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=False, resize_keyboard=True)
    if is_bot_English():
        itembtn_umbrella = types.KeyboardButton('/umbrella')
        itembtn_washingmachine = types.KeyboardButton('/washingmachine')
        itembtn_cold = types.KeyboardButton('/cold')
    else:
        itembtn_umbrella = types.KeyboardButton('/paraguas')
        itembtn_washingmachine = types.KeyboardButton('/lavadora')
        itembtn_cold = types.KeyboardButton('/frio')
    keyboard.add(itembtn_umbrella, itembtn_washingmachine, itembtn_cold)

    bot.send_message(message.chat.id, answer, reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def get_commands_help(message):
    """Shows a list of all the current commands"""
    response = HELP_ENG if is_bot_English() else HELP_VAL

    # Creating a custom keyboard to simplify the commands entering process
    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=False, resize_keyboard=True)
    if is_bot_English():
        itembtn_umbrella = types.KeyboardButton('/umbrella')
        itembtn_washingmachine = types.KeyboardButton('/washingmachine')
        itembtn_cold = types.KeyboardButton('/cold')
    else:
        itembtn_umbrella = types.KeyboardButton('/paraguas')
        itembtn_washingmachine = types.KeyboardButton('/lavadora')
        itembtn_cold = types.KeyboardButton('/frio')
    keyboard.add(itembtn_umbrella, itembtn_washingmachine, itembtn_cold)

    bot.send_message(message.chat.id, response, reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def start_and_ask_location(message):
    """Presents itself and asks for the user location"""

    # Setting a "Send location" keyboard button
    if is_bot_English():
        INTRODUCTION_MSG = INTRODUCTION_ENG
        itembtn_location = types.KeyboardButton("Of course I will, no problem bro!", request_location=True)
    else:
        INTRODUCTION_MSG = INTRODUCTION_VAL
        itembtn_location = types.KeyboardButton("Clar que sí home, el que faça falta!", request_location=True)

    keyboard = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True, resize_keyboard=True)
    keyboard.add(itembtn_location)
    bot.send_message(message.chat.id, INTRODUCTION_MSG, reply_markup=keyboard)


@bot.message_handler(regexp='^ping$')
def test_that_bot_works(message):
    bot.reply_to(message, 'ACK')


# Starting the bot
bot.polling(none_stop=True)
