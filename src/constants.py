# coding=utf-8
"""
File in which we store those values of the app that remain unchanged (sentences to answer, weather condition IDs...)
"""

"""
SECTION: WEATHER IDs.
Obtained from https://openweathermap.org/weather-conditions
"""
WEATHER_ID_CLEAR = 800

WEATHER_ID_FEW_CLOUDS = 801
WEATHER_ID_SCATTERED_CLOUDS = 802
WEATHER_ID_BROKEN_CLOUDS = 803
WEATHER_ID_OVERCAST_CLOUDS = 804

WEATHER_GROUP_CLOUDS = (
    WEATHER_ID_FEW_CLOUDS,
    WEATHER_ID_SCATTERED_CLOUDS,
    WEATHER_ID_BROKEN_CLOUDS,
    WEATHER_ID_OVERCAST_CLOUDS
)

WEATHER_ID_CALM = 951

# Contains every weather ID that represents that it isn't raining
WEATHER_GROUP_GOOD_WEATHER = (
    WEATHER_ID_CLEAR,
    WEATHER_ID_FEW_CLOUDS,
    WEATHER_ID_SCATTERED_CLOUDS,
    WEATHER_ID_BROKEN_CLOUDS,
    WEATHER_ID_OVERCAST_CLOUDS,
    WEATHER_ID_CALM
)

"""
SECTION: ANSWER SENTENCES
"""
INTRODUCTION_ENG = """Hi human! I'm @BadWeatherBot, the bot that will help you know if the weather will be bad in a \
                   specific moment. You have two different options: 
                   
                   If you need to know if you should take an umbrella today when going out, you can use the /umbrella \
                   command. It will indicate if it will rain, snow or anything similar in the following 24 hours.
                   
                   On the other hand, if you're planning to wash your clothes, then the /washingmachine command is for \
                   you! With it, you'll now if there will be any bad weather condition within 3 days, so you can decide \
                   if you should hang out the clothes or not.
                   
                   But first, in order to do this, I'll need to know your location. Would you mind sending it to me? """
TODAY_NO_WORRY_ENG = "Don't worry bro, the sun will shine today!"
TODAY_WORRY_ENG = "Bad news, today it's rain day..."
FORECAST_NO_WORRY_ENG = "Don't worry pal! The sun is shining and will keep doing it!"
FORECAST_WORRY_ENG = "You shouldn't do that, it will rain within 3 days"
LOW_TEMPERATURE_ENG = "Today's min temperature will be {} Celsius degrees. Now it's up to you to cover yourself or not"
LOCATION_STORED_CORRECTLY_ENG = "Location correctly updated!"
LOCATION_NOT_STORED_CORRECTLY_ENG = "Impossible to update location. Please try again later"
HELP_ENG = "/umbrella - Tells if the weather will be bad in the following 24 hours\n" \
    + "/washingmachine - Tells if the weather will be bad within 3 days"


INTRODUCTION_VAL = """Bon dia company! Soc @MalTiempoBot, el bot que et permetrà saber si farà mal temps pròximament. \
Disposes de dos opcions: 

Si necessites saber si deuries agafar paraigües hui per a ixir de casa, necessites el comando /paraguas. T'indicarà si \
durant les pròximes 24h plourà, nevarà, o qualsevol condició meteorològica similar.
 
Si el que necessites saber és si pots estendre tranquil o no, has d'utilitzar /lavadora. Amb este comando t'indicaré si \
ha de fer mal temps en algun moment durant els pròxims 3 dies, per a que no t'hages de preocupar de tindre que rentar \
dos voltes seguides la mateixa roba.

Però abans que res, per a poder funcionar correctament, necessite saber la teua ubicació. T'importa enviar-me-la?"""
TODAY_NO_WORRY_VAL = "Pots estar tranquil, que fa bon temps!"
TODAY_WORRY_VAL = "Males notícies... Si tens roba estesa, ja cal que la llaves altra volta"
FORECAST_NO_WORRY_VAL = "Pots estar tranquil, que fa i farà bon temps els pròxims 3 dies!"
FORECAST_WORRY_VAL = "Et recomane mirar bé el temps abans, ha de ploure en els pròxims 3 dies"
LOW_TEMPERATURE_VAL = 'Hui tindrem mínimes de {} graus. Tu voràs si abrigar-te o no...'
LOCATION_STORED_CORRECTLY_VAL = "Localització actualitzada correctament!"
LOCATION_NOT_STORED_CORRECTLY_VAL = "No s'ha pogut actualitzar la localització. Per favor, intenta-ho de nou en un altre moment"
HELP_VAL = "/paraguas - Indica si hace mal tiempo en este momento\n" \
    + "/lavadora - Indica si hará mal tiempo en los próximos 3 días"

