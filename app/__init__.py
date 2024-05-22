pip install Flask
pip install googlesearch-python

from flask import Flask, request

import time
from googlesearch import search

app = Flask(__name__)

# Ruta para procesar un dato individual
@app.route('/procesar_dato', methods=['GET'])
def procesar_dato():
    dato = request.args.get('dato')
    # Aquí llamas a tu función de procesamiento de Python
    resultado = procesar_dato_en_python(dato)
    return resultado

# Función de procesamiento en Python
def procesar_dato_en_python(dato):
    # Aquí va tu lógica de procesamient
    # Checar cada url en Google y registrar los resultados
    query = f'site:{item}'
    try:
        search_results = list(search(query))
        results = 1 if any(url in result for result in search_results) else 0
    except Exception as e:
        print(f'Error al buscar {url}. Error {e}')
        results = 0
        time.sleep(1)
    
    resultado = results
    return resultado

if __name__ == '__main__':
    app.run(debug=True)








if __name__ == '__main__':
    app.run(debug=True)
