from flask import Flask, jsonify, request
import requests
import json

app3 = Flask(__name__)

@app3.route('/<int:municipioid>/meteo/', methods=['GET'])
def get_meteo(municipioid):
    resp = f"https://www.el-tiempo.net/api/json/v2/provincias/14/municipios/{municipioid}"
    diccionario = requests.get(resp).json()
    diccionario_nuevo = {
        "temperatura" : diccionario["temperatura_actual"],
        "temperatura_maxima" : diccionario["temperaturas"]["max"],
        "temperatura_minima" : diccionario["temperaturas"]["min"],
        "humedad" : diccionario["humedad"],
        "viento" : diccionario["viento"],
        "precipitacion" : diccionario["precipitacion"],
        "lluvia" : diccionario["lluvia"]
       }
    if(diccionario["municipio"]["CODIGOINE"][0:5]==str(municipioid)):
            return jsonify(diccionario_nuevo)
    else:
            return "{\"info\": \"Meteorologia no disponible\"}"

if __name__ == '__main__':
    app3.run(port=5002)