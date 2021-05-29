from flask import Flask, request, make_response, jsonify
from datetime import datetime
import requests
from uuid import uuid4

app = Flask(__name__)

DB_URL = "http://localhost:5001/jobs"


@app.route("/", methods=["GET", "POST", "OPTIONS"])
def jobs():
    if request.method == "OPTIONS":  # CORS preflight
        return _build_cors_prelight_response()
    else:
        if request.method == "GET":
            resp = requests.get("http://localhost:5001/jobs")
            return _corsify_actual_response(resp.json(), resp.status_code)
        if request.method == "POST":
            try:
                employer_id = request.json["employerId"]
                title = request.json["title"]
                salary = request.json.get("salary")
                start_date = request.json.get("startDate")
                company = request.json["company"]
                sector = request.json.get("sector")
                description = request.json.get("description")
            except:
                return _corsify_actual_response(
                    jsonify({"Message": "Employer ID, Title, and Companyare required"}),
                    400,
                )

            job = {
                "id": str(uuid4()),
                "employerId": employer_id,
                "title": title,
                "salary": salary,
                "startDate": start_date,
                "company": company,
                "sector": sector,
                "description": description,
            }

            response = requests.post(DB_URL, job)

            return _corsify_actual_response(response.json(), response.status_code)


@app.route("/<id>", methods=["GET", "DELETE", "OPTIONS"])
def job(id):
    if request.method == "OPTIONS":  # CORS preflight
        return _build_cors_prelight_response()
    else:
        if request.method == "GET":
            resp = requests.get(f"{DB_URL}/{id}")
            return _corsify_actual_response(resp.json(), resp.status_code)
        if request.method == "DELETE":
            resp = requests.delete(f"{DB_URL}/{id}")
            return _corsify_actual_response(resp.json(), resp.status_code)


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
    app.run(debug=True, port=5000)