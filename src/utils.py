import os
import psycopg2


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
    conn = psycopg2.connect(DB_URI)


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


def store_user_location(user, location):
    """
    Gets a user and its location and stores them in the DB
    """

    # Extracting the necessary parameters from the input
    userid = user.id
    lon = location.longitude
    lat = location.latitude

    # Getting the cursor to operate with the DB
    cur = get_db_cursor()

    # Storing the data
    SQL_QUERY = """
                INSERT INTO user_location (user_id, longitude, latitude) VALUES ({user_id}, {longitude}, {latitude})
                """.format(user_id=userid, longitude=lon, latitude=lat)
    cur.execute(SQL_QUERY)

    # Saving changes to the DB and closing the connection
    cur.connection.commit()
    close_db_from_cursor(cur)

    return True

