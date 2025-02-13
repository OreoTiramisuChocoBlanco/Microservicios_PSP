from flask import Flask, jsonify, abort
import json

app1 = Flask(__name__)

@app1.route("/<int:municipioid>/geo/")
def get_geo(municipioid):
    with open("municipio.json") as json_municipio:
        diccionario = json.load(json_municipio)
        print(diccionario["codigo"], municipioid)
        if (diccionario["codigo"] == municipioid):
            return jsonify(diccionario) 
        else:
            abort(404)
            #return "{\"info\": \"Municipio no disponible\"}"

if __name__ == '__main__':
    app1.run(port=5000)