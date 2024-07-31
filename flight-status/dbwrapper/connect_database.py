import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
class ConnectDatabase:
    """
    Creates a connection with the mongo database.
    """

    def __init__(self):
        """configure database"""
        self.connection = MongoClient(os.getenv('mongo_connection_string'))
        self.database = self.connection[os.getenv('dbname')]

    def close_connection(self):
        self.connection.close()
