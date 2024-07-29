import json

from flask import Flask, request, Response
from apis.users import users_api
from apis.flight import flight_api
from flask_cors import CORS # type: ignore

# # from error_handlers import error_blueprint (to integrate error handlers if needed)
#
app = Flask(__name__)
CORS(app)
app.register_blueprint(users_api)
app.register_blueprint(flight_api)


@app.route("/home", methods=['GET'])
def hello():
    return "Welcome to indigo"


if __name__ == "__main__":
    # Only for debugging while developing

    app.run(host='0.0.0.0', debug=True)