from flask import Flask, jsonify, abort, request
import json
import requests

app4 = Flask(__name__)

@app4.route("/<int:municipioid>/<parametro1>/")
@app4.route("/<int:municipioid>/<parametro1>/<parametro2>/")
@app4.route("/<int:municipioid>/<parametro1>/<parametro2>/<parametro3>/")
def get_json(municipioid, parametro1="", parametro2="", parametro3=""):
    with open("municipio.json") as json_municipio:
        diccionario = json.load(json_municipio)
        if (diccionario["codigo"] == municipioid):
            path = request.path
            if "geo" in path:
                diccionario.update(requests.get(f"http://servicio1:5000/{municipioid}/geo/").json())

            if "demo" in path:
                print("demo")
                diccionario.update(requests.get(f"http://servicio2:5001/{municipioid}/demo/").json())

            if "meteo" in path:
                print("meteo")
                diccionario.update(requests.get(f"http://servicio3:5002/{municipioid}/meteo/").json())

            return jsonify(diccionario) 
        else:
            abort(404)

if __name__ == '__main__':
    app4.run(port=5003)