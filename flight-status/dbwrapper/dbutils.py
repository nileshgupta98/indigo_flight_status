import os, datetime, traceback
from bson.objectid import ObjectId
from exceptions import CustomErrors
from dbwrapper.connect_database import ConnectDatabase

db_connection = ConnectDatabase()

def insert_documents(collection_name, documents_to_insert, many):
    """To Insert data in DB based on collection
    :param collection_name: MongoDb collection name
    :param documents_to_insert: array containing all the documents that need to be inserted in db in case of multiple
    documents, dictonary in case of single document
    """
    try:
        collection = db_connection.database[collection_name]
        # condition used for documents insert using inser_many fuction
        if many:
            inserted_docs = collection.insert_many(documents_to_insert)
            id = inserted_docs.inserted_ids
            return id
        else:
            inserted_docs = collection.insert_one(documents_to_insert)
            id = inserted_docs.inserted_id
            return id
        # print list of the _id values of the inserted documents:

    # Handle exceptions:
    except Exception as e:

        raise CustomErrors("Unknown Error occurred.", 500)


def fetch_documents(collection_name, condition=None, one=None, columns=None, sort_condition=None):
    """To fetch data from DB based on collection and document id
    :param collection_name:str MongoDb collection name
    :param condition:dict search condition
    :param columns: specify which column data is required
    """
    try:
        collection = db_connection.database[collection_name]
        # condition used for documents fetch using condition or not
        if one:
            if condition and columns:
                documents = collection.find_one(condition, columns)
                return documents
            elif condition:
                documents = collection.find_one(condition)
                return documents
        else:
            if condition and columns:
                documents = collection.find(condition, columns)
                return documents
            elif condition and sort_condition:
                documents = collection.find(condition).sort(sort_condition[0], sort_condition[1])
                return documents
            elif condition:
                documents = collection.find(condition)
                return documents
            else:
                documents = collection.find()
                return documents

    # Handle exceptions:
    except Exception as e:

        raise CustomErrors("Unknown Error occurred.", 500)


def update_docs(collection_name, condition, update_query, upsert=None,many=None):
    """To update data in DB based on collection and condition
    :param collection_name:str MongoDb collection name
    :param condition:dict condition for to which documents will get updated
    :param update_query:dict query which includes what needs to updated
    :param upsert:boolean with the help of this we set the value of upsert parameter in update_one function    """
    try:
        if many:
            if upsert:
                collection = db_connection.database[collection_name]
                updated_docs = collection.update_many(condition, update_query, upsert=upsert)
                return True
            else:
                collection = db_connection.database[collection_name]
                updated_docs = collection.update_many(condition, update_query)
                return True
        else:
            if upsert:
                collection = db_connection.database[collection_name]
                updated_docs = collection.update_one(condition, update_query, upsert=upsert)
                return True
            else:
                collection = db_connection.database[collection_name]
                updated_docs = collection.update_one(condition, update_query)
                return True
    # Handle exceptions:
    except Exception as e:

        raise CustomErrors("Unknown Error occurred.", 500)


def get_document_count(collection_name, condition={}):
    """To get the count of rows in db that satisfy the condition
        :param collection_name:str MongoDb collection name
        :param condition:dict condition on which count will be calculated"""
    try:
        collection = db_connection.database[collection_name]
        count = collection.count_documents(condition)
        return count
    # Handle exceptions:
    except Exception as e:

        raise CustomErrors("Unknown Error occurred.", 500)


def aggregate_data(collection_name, aggregate_condition):
    """To get the count of rows in db that satisfy the condition
        :param collection_name:str MongoDb collection name
        :param aggregate_condition:list condition on which aggregation will be done"""
    try:
        collection = db_connection.database[collection_name]
        docs = collection.aggregate(aggregate_condition)
        return docs
    # Handle exceptions:
    except Exception as e:

        raise CustomErrors("Unknown Error occurred.", 500)


def bulk_operations(collection_name, operations):
    """To perform bulk operations in mongodb"""
    try:
        collection = db_connection.database[collection_name]
        docs = collection.bulk_write(operations)
        return docs
    # Handle exceptions:
    except Exception as e:

        raise CustomErrors("Unknown Error occurred.", 500)


def delete_document(collection_name,condition):
    """
    To perform delete operation
    """
    try:
        collection = db_connection.database[collection_name]
        collection.delete_one(condition)
    # Handle exceptions:
    except Exception as e:

        raise CustomErrors("Unknown Error occurred.", 500)
