from flask import Flask, request, make_response, jsonify
import requests
import bcrypt

DB_URL = "http://db-service/employers"

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
            return _corsify_actual_response(
                jsonify({"Message": "Cannot find user"}), 400
            )

        employer = employers[0]
        hashed_pw = employer["password"]

        if bcrypt.checkpw(bytes(password, "utf-8"), bytes(hashed_pw, "utf-8")):
            return _corsify_actual_response(jsonify({"id": employer["id"]}), 200)

        return _corsify_actual_response(jsonify({"Message": "Invalid"}), 400)


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
    app.run(host="0.0.0.0", port=80)
