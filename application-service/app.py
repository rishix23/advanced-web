from flask import Flask, request, make_response, jsonify
import requests
from uuid import uuid4

DB_URL = "http://db-service/applications"

app = Flask(__name__)


@app.route("/", methods=["POST", "OPTIONS"])
def confirmApplication():
    # CORS preflight
    if request.method == "OPTIONS":
        return _build_cors_prelight_response()
    # The actual request following the preflight
    if request.method == "POST":
        try:
            job_id = request.form.get("jobId")
            full_name = request.form.get("fullname")
            phone = request.form.get("phone")
            email = request.form.get("email")
            resume = request.files.get("resume")
        except:
            return _corsify_actual_response(
                jsonify(
                    {"message": "JobID, Fullname, Phone, Email and Resume are required"}
                )
            )

        application = {
            "id": str(uuid4()),
            "jobId": job_id,
            "fullname": full_name,
            "phone": phone,
            "email": email,
        }

        response = requests.post(DB_URL, application, files={"resume": resume.read()})

        if not response.ok:
            return _corsify_actual_response(
                jsonify({"Message": "Something went wrong, please try again later"})
            )

        return _corsify_actual_response(response.json())


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
    app.run(host="0.0.0.0", port=80)
