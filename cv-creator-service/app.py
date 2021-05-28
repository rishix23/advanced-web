from flask import (
    Flask,
    request,
    render_template,
    Response,
    make_response,
    jsonify,
    send_file,
)
from datetime import datetime
from docx import Document
import cv_creator as cv
import io
from io import BytesIO

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/CVTemplate1", methods=["POST", "OPTIONS"])
def createTemplate1():

    # CORS preflight
    if request.method == "OPTIONS":
        return _build_cors_prelight_response()
    # The actual request following the preflight
    elif request.method == "POST":

        json_object = request.json
        print(json_object)

        document = cv.template1(json_object)
        f = io.BytesIO()
        document.save(f)
        length = f.tell()
        f.seek(0)

        response = send_file(f, as_attachment=True, attachment_filename="cv.doc")

        return _corsify_actual_response(response)


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
    app.run()

# git branch "name" /
# git checkout "name"/
# git add ./
# git commit -m/
# git push "name"