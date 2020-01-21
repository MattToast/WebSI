import os
from flask import jsonify


def countFiles():
    listFiles = []
    for file in os.listdir('../../'):
        listFiles.append(file)

    print(listFiles)

if __name__ == '__main__':
    countFiles()
