from flask import Flask, jsonify
import requests
import json

app3 = Flask(__name__)

@app3.route('/<int:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    resp = requests.get("https://www.el-tiempo.net/api/json/v2/provincias/14/municipios/14037")
    diccionario = resp.json()
    if(diccionario["municipio"]["CODIGOINE"][0:5]==str(municipioid)):
            return jsonify(diccionario)
    else:
            return "{\"info\": \"Meteorologia no disponible\"}"

if __name__ == '__main__':
    app3.run(port=5002)