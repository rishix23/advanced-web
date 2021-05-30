from io import BytesIO
from flask import Flask, request, make_response, send_file, jsonify
import requests
from uuid import uuid4

DB_URL = "http://db-service/applications"

app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "OPTIONS"])
def index():
    # CORS preflight
    if request.method == "OPTIONS":
        return _build_cors_prelight_response()
    # The actual request following the preflight
    if request.method == "GET":
        if request.args.get("jobId"):
            response = requests.get(f"{DB_URL}?jobId={request.args['jobId']}")
            return _corsify_actual_response(
                jsonify(response.json()), response.status_code
            )
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
                    {
                        "Message": "JobID, Fullname, Phone, Email and Resume are required"
                    },
                    400,
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
                jsonify({"Message": "Something went wrong, please try again later"}),
                response.status_code,
            )

        return _corsify_actual_response(jsonify(response.json()), response.status_code)


@app.route("/<id>", methods=["POST", "OPTIONS"])
def download(id):
    if request.method == "OPTIONS":
        return _build_cors_prelight_response()
    if request.method == "POST":
        resp = requests.post(f"{DB_URL}/{id}")
        response = send_file(
            BytesIO(resp.content),
            as_attachment=True,
            attachment_filename=resp.headers["Content-Disposition"]
            .split(" ", 1)[1]
            .split("=")[1]
            .replace('"', "")
            .replace("'", ""),
        )

        return _corsify_actual_response(response)


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
