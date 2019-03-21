import flask
from flask import request
import re
flask
app = flask.Flask(__name__)
@app .route("/")
def hello():
    return "Kevin Belajar Flask"

@app.route("/music")
def music():
    return "Music. where is Music? Cokelat!!!"
@app.route("/login", methods = ['GET', 'POST', 'DELETE'])
def login_html():
    print("--------------")
    print(request.method)
    print("--------------")
    print(request.form)
    post = "%s" %(request.form)
    with open("loginnet.html") as oke:
        return oke.read()

if __name__ == "__main__":
    app.static_folder = "/root/programming/python_saya/static"
    app.run(debug=True, port=8080, host="0.0.0.0")
    
