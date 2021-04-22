from flask import Flask

app = Flask("Jobs Service")


@app.route("/")
def index():
    return "Index"


if __name__ == "__main__":
    app.run(debug=True)