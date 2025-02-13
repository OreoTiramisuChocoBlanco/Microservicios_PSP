from flask import Flask, jsonify
import json

app1 = Flask(__name__)

@app1.route("/<int:municipioid>/geo")
def get_geo(municipioid):
    with open("municipio.json") as json_municipio:
        diccionario = json.load(json_municipio)
        if (diccionario["codigo"] == municipioid):
            return jsonify(diccionario) 
        else:
            return "{\"info\": \"Municipio no disponible\"}"

if __name__ == '__main__':
    app1.run(port=5000)