from flask import Flask, request, jsonify
import time  # Asegúrate de importar cualquier módulo necesario
from googlesearch import search

app = Flask(__name__)


def procesar_dato(dato):
    # Procesar el dato aquí (este es solo un ejemplo simple)
    
    # Checar cada url en Google y registrar los resultados
    query = f'site:{dato}'
    try:
        search_results = list(search(query))
        results = 1 if any(dato in result for result in search_results) else 0
    except Exception as e:
        #print(f'Error al buscar {url}. Error {e}')
        results = 0
        time.sleep(1)
    
    resultado = results
    return resultado



@app.route('/procesar_dato', methods=['POST'])
def procesar_dato_route():
    data = request.get_json()
    dato = data['dato']
    resultado = procesar_dato(dato)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)
