from flask import Flask, request, make_response
from flask.json import jsonify
from flask.wrappers import Response
import requests
import bcrypt

DB_URL = "http://localhost:5001/employers"

app = Flask(__name__)


@app.route("/", methods=["POST", "OPTIONS"])
def employers():
    if request.method == "OPTIONS":  # CORS preflight
        return _build_cors_prelight_response()
    else:
        email = request.json.get("email", "")
        password = request.json.get("password", "")

        employers = requests.get(f"{DB_URL}?email={email}").json()
        if len(employers) < 1:
            return _corsify_actual_response(Response("Cannot find user", 400))

        employer = employers[0]
        hashed_pw = employer["password"]

        if bcrypt.checkpw(bytes(password, "utf-8"), bytes(hashed_pw, "utf-8")):
            return _corsify_actual_response(Response(employer["id"], 200))

        return _corsify_actual_response(Response("Invalid", 400))


def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5004)