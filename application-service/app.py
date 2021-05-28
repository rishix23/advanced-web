from flask import Flask, render_template, request
from models import Application

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
        job_id = request.id
        full_name = request.fullname
        phone = request.phone
        email = request.email

        file_ = request.file('filename')
        newFile = FileContents(name="test", data=file.read())
        db.session.add(newFile)
        db.session.commit()


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