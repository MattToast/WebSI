from flask import Flask, render_template, request, jsonify
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
    return jsonify({"files" : listFiles})
 
if __name__ == "__main__":
    app.run()
    print("\nApplication Terminated")