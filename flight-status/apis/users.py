import json, traceback
from flask import Blueprint, Response, request
from exceptions import CustomErrors
# import config
from bson import ObjectId
from dbwrapper import dbutils
from pathlib import Path
import os
import shutil
from utils import users

users_api = Blueprint("users", __name__)


@users_api.route("/users/login", methods=['POST'])
def user_login():
    """
    To get historic and current documents uploaded by the particular user
    """
    try:
        data = request.get_json()
        response = users.login(data)
        if response:
            response_payload = {
                "message": "Login successfully",
                "response": True,
                "user_id": response,
                "status": 200
            }
            return Response(json.dumps(response_payload),
                            mimetype="application/json",
                            status=200)
        else:
            response_payload = {
                "message": "email or password is wrong",
                "response": False,
                "status": 401
            }
            return Response(json.dumps(response_payload),
                            mimetype="application/json",
                            status=401)

    except KeyError as key_error:
        response_payload = {"message": "Missing Data",
                            "detail": key_error.__str__(),
                            "status": 500}
        return Response(json.dumps(response_payload),
                        mimetype="application/json",
                        status=400)

    except CustomErrors as error:
        response_payload = {"message": "Error encountered",
                            "response": error.message,
                            "status": error.status_code}
        return Response(json.dumps(response_payload),
                        mimetype="application/json",
                        status=error.status_code)

    


