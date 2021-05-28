from flask import Flask, render_template, request
import requests
from models import Application

DB_URL = 'http://localhost:5000/applications'

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")

@app.route("/confirmApplication", methods=['POST', "OPTIONS"])
def confirmApplication():
     # CORS preflight
    if request.method == "OPTIONS":
        return _build_cors_prelight_response()
    # The actual request following the preflight
    elif request.method == "POST":
        print(request) 

        data = {}

        data["jobId"] = request.form.get("jobId")
        data["fullname"] = request.form.get("fullname")
        data["phone"] = request.form.get("phone")
        data["email"] = request.form.get("email")
        # data['resume'] = request.files.get('resume')
        # data[newFile] = FileContents(name="test", data=file_.read())

        file_ = request.files.get('resume')

        print("FILE:")
        print(file_)

    
        file_.seek(0)

        file_data = file_.read()

        # files = {'file': open(file_, 'rb')}
        # r = requests.post(url, files=files)
    
        response = requests.post(DB_URL, data, files={'file_test': file_data})

        # requests.post(DB_URL, data)

        # db.session.add(newFile)
        # db.session.commit()
        return _corsify_actual_response(response)
  
def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    app.run(debug=True, port=5003)

# POST user application to job
# check frontend request 
# -job id
# -fullname
# -email
# -phone

# store in db 

# -cv pdf 

# store in db as byte conversion 

# need back:

# -everything went ok

# For now, just needs a post which takes in a job id parameter, full name, email, phone, cv document
# https://www.youtube.com/watch?v=TLgVEBuQURA might help with storing the cv into the db