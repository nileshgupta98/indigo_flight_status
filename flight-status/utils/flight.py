import os, datetime, traceback
from bson.objectid import ObjectId
from exceptions import CustomErrors
from dbwrapper import dbutils

def flight_status(flight_num):
    try:
        flight_data = dbutils.fetch_documents(collection_name="flight_data",
                                       condition={"flight_id": flight_num},
                                       one=True)
        return flight_data

    # Handle exceptions:
    except:

        raise CustomErrors("Unknown Error occurred.", 500)


