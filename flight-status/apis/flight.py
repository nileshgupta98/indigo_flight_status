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
from utils import flight

flight_api = Blueprint("flight", __name__)


@flight_api.route("/flight/status", methods=['GET'])
def flight_status():
    """
    To get historic and current documents uploaded by the particular user
    """
    try:
        flight_num = request.args.get("flight_num")
        print(flight_num)
        response = flight.flight_status(flight_num)
        if response:
            data = {'status':response['status'],
                    'departure_gate':response['departure_gate'],
                    'arrival_gate':response['arrival_gate'],
                    'scheduled_departure':str(response['scheduled_departure']),
                    'scheduled_arrival':str(response['scheduled_arrival']),
                    'actual_departure':str(response['actual_departure']),
                    'actual_arrival':str(response['actual_arrival'])}
            response_payload = {
                "message": "Data Found",
                "data":data,
                "response": True,
                "status": 200
            }
            return Response(json.dumps(response_payload),
                            mimetype="application/json",
                            status=200)
        else:
            response_payload = {
                "message": "Data Not Found",
                "response": False,
                "status": 404,
                "data":{}
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

    



