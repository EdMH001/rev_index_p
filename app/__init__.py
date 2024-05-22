from flask import Flask, request, jsonify
from prosc_datos import procesar_dato

import time
from googlesearch import search

app = Flask(__name__)

@app.route('/procesar_dato', methods=['POST'])
def procesar_dato_route():
    data = request.get_json()
    dato = data['dato']
    resultado = procesar_dato(dato)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
