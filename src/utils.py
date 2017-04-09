import os
import psycopg2
from psycopg2._psycopg import ProgrammingError

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

def get_user_location(user):
    """
    Gets an user and retrieves its location from the DB.
    
    The location is returned as a tuple containing (Lat, Lon). If we don't have any location for the current user, 
    returns (-1, -1)
    """

    # Extracting the necessary parameters from the input
    userid = user.id

    cur = get_db_cursor()

    # Querying the DB
    SQL_QUERY = """
                SELECT latitude, longitude FROM user_location WHERE userid={userid}
                """.format(userid=userid)
    cur.execute(SQL_QUERY)

    try:
        row = cur.fetchone()
        lat = row[0]
        lon = row[1]
    except ProgrammingError:  # There isn't any data in the cursor (i.e. we don't have any location for the user)
        lat = -1
        lon = -1
    finally:
        # Closing connection
        close_db_from_cursor(cur)
        return (lat, lon)
    



def store_user_location(user, location):
    """
    Gets a user and its location and stores them in the DB. Returns True if everything went as expected
    """

    # Extracting the necessary parameters from the input
    userid = user.id
    lon = location.longitude
    lat = location.latitude

    # Getting the cursor to operate with the DB
    cur = get_db_cursor()

    # Do we have any location data for the current user?
    if get_user_location(user) == (-1, -1):
        # If we don't, we'll insert the info
        SQL_QUERY = """
                    INSERT INTO user_location (userid, longitude, latitude) VALUES ({userid}, {longitude}, {latitude})
                    """.format(userid=userid, longitude=lon, latitude=lat)
    else:
        # If we do, we'll update the record
        SQL_QUERY = """
                    UPDATE user_location SET latitude = {latitude}, longitude = {longitude} WHERE userid = {userid}
                    """.format(userid=userid, longitude=lon, latitude=lat)


    cur.execute(SQL_QUERY)

    # Saving changes to the DB and closing the connection
    cur.connection.commit()
    close_db_from_cursor(cur)

    return True

