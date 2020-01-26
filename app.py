from flask import Flask, render_template, request, jsonify, redirect
import os

app = Flask(__name__)


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
def uploadFiles():
    if request.method == "POST":
        if request.files and request.files["image"]:
            image = request.files["image"]
            image.save(os.path.join("static/res/share/", image.filename))

            return redirect(request.url)

    return render_template('control.html')


if __name__ == "__main__":
    if not os.path.exists("./static/res/share/"):
        os.mkdir("./static/res/share/")

    app.run(host='0.0.0.0', port=8080)
    print("\nApplication Terminated")
