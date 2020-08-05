from flask import Flask, render_template, request, jsonify, redirect, make_response
from functools import wraps
import hashlib
import json
import os

# create a flask app
app = Flask(__name__)

# basic paths to use
appDir = '/home/mrdro/purdue/si/mattWebSI'
shareDir = os.path.join(appDir, "static/res/share/")


def check_auth(username, password):
    # check that a provided user name and password match the json
    try:
        with open(os.path.join(appDir, 'admin.json'), 'r') as jsonData:
            data = jsonData.read()
        obj = json.loads(data)
        compU = str(hashlib.sha256(username.encode()).hexdigest())
        compP = str(hashlib.sha256(password.encode()).hexdigest())
        return compU == obj['username'] and compP == obj['password']
    except Exception:
        return username == 'username' and password == 'password'


def authenticate():
    # simple failed login page
    return make_response("Could not verify your login!", 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route("/")
def start():
    # return the index page
    return render_template('index.html')


@app.route('/files', methods=['POST'])
def getFiles():
    # page needs list of files avalible for download
    # create list (in reverse order) and make a json
    # return the list
    listFiles = []
    for file in os.listdir(shareDir):
        listFiles.append(file)
    listFiles.sort(reverse=True)
    return jsonify({"files": listFiles})


@app.route('/control', methods=["GET", "POST"])
@auth_required
def updateFiles():
    # if post request is made
    if request.method == "POST":
        if request.files and request.files["upload"]:
            # user is attempting to upload a file
            # save it to share dir and redirect
            upload = request.files["upload"]
            upload.save(os.path.join(shareDir, upload.filename))
            return redirect(request.url)

        elif request.form and request.form["delete"]:
            # user is attempting to delete one or more file
            # iterate through and remove files if they exist
            # finally redirect
            file_names = dict(request.form)
            for file in file_names.values():
                if os.path.isfile(os.path.join(shareDir, file)):
                    os.remove(os.path.join(shareDir, file))

            return redirect(request.url)
    return render_template('control.html')


if __name__ == "__main__":
    # setup locally for testing
    # check that a share dire exists, if it doesn't create it
    if not os.path.exists("./static/res/share/"):
        os.mkdir("./static/res/share/")

    # luanch the app, print a message when closed
    app.run(host='localhost', port=8080)
    print("\nApplication Terminated")
