from flask import Flask, render_template, request, jsonify, redirect, make_response
from functools import wraps
import os

app = Flask(__name__)


def check_auth(username, password):
    return username == 'a' and password == 's'


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
    for file in os.listdir("static/res/share/"):
        listFiles.append(file)
    return jsonify({"files": listFiles})


@app.route('/control', methods=["GET", "POST"])
@auth_required
def updateFiles():
    if request.method == "POST":
        if request.files and request.files["upload"]:
            upload = request.files["upload"]
            upload.save(os.path.join("static/res/share/", upload.filename))

            return redirect(request.url)

        elif request.form and request.form["filename"]:
            filename = request.form["filename"]
            if os.path.isfile(os.path.join("static/res/share/", filename)):
                os.remove(os.path.join("static/res/share/", filename))

            return redirect(request.url)

    return render_template('control.html')


if __name__ == "__main__":
    if not os.path.exists("./static/res/share/"):
        os.mkdir("./static/res/share/")

    app.run(host='0.0.0.0', port=8080)
    print("\nApplication Terminated")
