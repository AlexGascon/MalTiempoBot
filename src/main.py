# -*- coding: utf-8 -*-   
import telebot
import os

from utils import store_user_location, get_user_location, ask_user_location
from weather import get_current_weather_in_location, is_bad_weather, get_5day_forecast_in_location, \
    get_today_forecast_in_location

# Creating the bot
TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN') # Token previously stored in an environment var
bot = telebot.TeleBot(TOKEN)


# The decorator (@bot.message_handler) indicates the type of messages that will activate this function
@bot.message_handler(commands=['paraguas'])
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

    if True in I_need_to_worry:
        bot.reply_to(message, 'Males notícies... Si tens roba estesa, ja cal que la llaves altra volta')
    else:
        bot.reply_to(message, 'Pots estar tranquil, que fa bon temps!')


@bot.message_handler(commands=['lavadora'])
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
        bot.reply_to(message, 'Et recomane mirar bé el temps abans, ha de ploure en els pròxims 5 dies')
    else:
        bot.reply_to(message, 'Pots estar tranquil, que fa i farà bon temps!')


@bot.message_handler(content_types=['location'])
def update_user_location(message):
    """Saves or updates the location for the current user"""
    location_stored_correctly = store_user_location(message.from_user, message.location)

    if location_stored_correctly:
        bot.reply_to(message, "Localització actualitzada correctament!")
    else:
        bot.reply_to(message, "No s'ha pogut actualitzar la localització. Per favor, intenta-ho de nou en un altre moment")


@bot.message_handler(commands=['start', 'help'])
def get_commands_help(message):
    """Shows a list of all the current commands"""
    response = """
    /lluvia - Indica si hace mal tiempo en este momento\n
    /lavadora - Indica si hará mal tiempo en los próximos 5 días
    """
    bot.reply_to(message, response)

@bot.message_handler(regexp='^ping$')
def test_that_bot_works(message):
    bot.reply_to(message, 'ACK')

# Starting the bot
bot.polling(none_stop=True)
