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
TODAY_NO_WORRY_ENG = "Don't worry bro, the sun will shine today!"
TODAY_WORRY_ENG = "Bad news, today it's rain day..."
FORECAST_NO_WORRY_ENG = "Don't worry pal! The sun is shining and will keep doing it!"
FORECAST_WORRY_ENG = "You should with more detail to the weather, it will rain within 5 days"
LOCATION_STORED_CORRECTLY_ENG = "Location correctly updated!"
LOCATION_NOT_STORED_CORRECTLY_ENG = "Impossible to update location. Please try again later"
HELP_ENG = "/umbrella - Tells if the weather will be bad in the following 24 hours\n" \
    + "/washingmachine - Tells if the weather will be bad within 3 days"

TODAY_NO_WORRY_VAL = "Pots estar tranquil, que fa bon temps!"
TODAY_WORRY_VAL = "Males notícies... Si tens roba estesa, ja cal que la llaves altra volta"
FORECAST_NO_WORRY_VAL = "Pots estar tranquil, que fa i farà bon temps els pròxims 5 dies!"
FORECAST_WORRY_VAL = "Et recomane mirar bé el temps abans, ha de ploure en els pròxims 5 dies"
LOCATION_STORED_CORRECTLY_VAL = "Localització actualitzada correctament!"
LOCATION_NOT_STORED_CORRECTLY_VAL = "No s'ha pogut actualitzar la localització. Per favor, intenta-ho de nou en un altre moment"
HELP_VAL = "/paraguas - Indica si hace mal tiempo en este momento\n" \
    + "/lavadora - Indica si hará mal tiempo en los próximos 3 días"

