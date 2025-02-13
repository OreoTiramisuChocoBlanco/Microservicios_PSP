from flask import Flask, jsonify, abort
import json

app2 = Flask(__name__)

@app2.route('/<int:municipioid>/demo', methods=['GET'])
def get_demo(municipioid):
    with open("municipio.json") as municipio_json:
        diccionario = json.load(municipio_json)
        if(diccionario["codigo"]==municipioid):
            return jsonify(diccionario)
        else:
            abort(404)
            #return "{\"info\": \"Municipio no disponible\"}"


if __name__ == '__main__':
    app2.run(port=5001)