import os, datetime, traceback
from bson.objectid import ObjectId
from exceptions import CustomErrors
from dbwrapper import dbutils

def login(data):
    """
    DESCRIPTION:
    check user credential
    for now we store static user id
    :param data: dict
    data contain email and password of user
    :return user_id: str
    user_id is reference id of user
    """
    try:
        user = dbutils.fetch_documents(collection_name="users",
                                       condition={"email_id": data['email']},
                                       one=True)
        if user:
            if user['password'] == data['password']:
                return str(user['_id'])
        else:
            return ''

    # Handle exceptions:
    except:

        raise CustomErrors("Unknown Error occurred.", 500)


