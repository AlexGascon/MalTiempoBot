import os
import psycopg2


"""API SECTION"""
def get_OpenWeatherAPI_token():
    # Setting the API Key
    TOKEN = os.environ.get('OPENWEATHERMAP_TEST_TOKEN')
    # TOKEN = os.environ.get('OPENWEATHERMAP_PRODUCTION_TOKEN')

    return TOKEN

"""DATABASE SECTION"""
def get_db_cursor():
    """
    Connects to the database and returns the cursor to use to interact with it
    """
    DB_URI = os.environ.get('DATABASE_URL')
    

    pass

def store_user_location():
    """

    """