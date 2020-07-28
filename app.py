from flask import Flask, render_template, request, jsonify, redirect, make_response
from functools import wraps
import hashlib
import json
import os

app = Flask(__name__)

appDir = '/home/mrdro/purdue/si/mattWebSI'
shareDir = os.path.join(appDir, "static/res/share/")

def check_auth(username, password):
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
    return render_template('index.html')


@app.route('/files', methods=['POST'])
def getFiles():
    listFiles = []
    for file in os.listdir(shareDir):
        listFiles.append(file)
    listFiles.sort(reverse=True)
    return jsonify({"files": listFiles})


@app.route('/control', methods=["GET", "POST"])
@auth_required
def updateFiles():
    if request.method == "POST":
        if request.files and request.files["upload"]:
            upload = request.files["upload"]
            upload.save(os.path.join(shareDir, upload.filename))

            return redirect(request.url)

        elif request.form and request.form["filename"]:
            filename = request.form["filename"]
            print(request.form["filename"])
            if os.path.isfile(os.path.join(shareDir, filename)):
                os.remove(os.path.join(shareDir, filename))

            return redirect(request.url)

    return render_template('control.html')


if __name__ == "__main__":
    if not os.path.exists("./static/res/share/"):
        os.mkdir("./static/res/share/")

    app.run(host='localhost', port=8080)
    print("\nApplication Terminated")
