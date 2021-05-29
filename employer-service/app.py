from flask import Flask, request, make_response, jsonify, Response
from datetime import datetime
import bcrypt
import requests
from uuid import uuid4

DB_URL = "http://localhost:5001/employers"

app = Flask(__name__)


@app.route("/", methods=["POST", "OPTIONS"])
def employers():
    if request.method == "OPTIONS":  # CORS preflight
        return _build_cors_prelight_response()
    else:
        try:
            first_name = request.json["firstName"]
            last_name = request.json["lastName"]
            email = request.json["email"]
            password = request.json["password"]
        except:
            return _corsify_actual_response(
                jsonify(
                    {
                        "Message": "First Name, Last Name, Email and Password are required"
                    }
                ),
                400,
            )

        existing_employer = requests.get(f"{DB_URL}?email={email}").json()

        if existing_employer:
            return _corsify_actual_response(
                jsonify({"Message": "User with the supplied email already exists"}), 400
            )

        id = str(uuid4())
        employer = {
            "id": id,
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "password": bcrypt.hashpw(
                bytes(password, "utf-8"), bcrypt.gensalt()
            ).decode("utf-8"),
        }

        response = requests.post(DB_URL, json=employer)

        if not response.ok:
            return _corsify_actual_response(
                jsonify({"Message": "Something went wrong, please try again later"}),
                500,
            )
        return _corsify_actual_response(jsonify({"id": id}), 201)


def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Methods", "*")
    return response


def _corsify_actual_response(response, status_code=200):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.status_code = status_code
    return response


if __name__ == "__main__":
    app.run(debug=True, port=5005)