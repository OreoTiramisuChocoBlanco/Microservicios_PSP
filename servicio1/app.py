from flask import Flask, jsonify
import json

app1 = Flask(__name__)



if __name__ == '__main__':
    app1.run(port=5000)