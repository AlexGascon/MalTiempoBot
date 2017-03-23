import os


"""
API SECTION
"""
def get_OpenWeatherAPI_token():
    # Setting the API Key
    TOKEN = os.environ.get('OPENWEATHERMAP_TEST_TOKEN')
    # TOKEN = os.environ.get('OPENWEATHERMAP_PRODUCTION_TOKEN')

    return TOKEN

"""
DATABASE SECTION
"""
def get_db_cursor():
    """
    Connects to the database and returns the cursor to use to interact with it
    """

    # Obtaining the database URL from the environment variables
    DB_URI = os.environ.get('DATABASE_URL')

    # Connecting to the DB
    try:
        conn = psycopg2.connect(DB_URI)
    except:
        return -1

    # Open a cursor to perform database operations
    cur = conn.cursor()

    return cur

def close_db_from_cursor(cursor):
    """
    Gets a DB cursor and closes it and its associated DB.

    Returns True if everything went as expected and False otherwise
    """
    try:
        connection = cursor.connection
        cursor.close()
        connection.close()
    except:
        return False

    return True

