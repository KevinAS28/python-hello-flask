import flask

app = flask.Flask(__name__)
@app.route("/")
def hello():
    return "Kevin Belajar Flask"
if __name__ == "__main__":
    app.run(debug=True)