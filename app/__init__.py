pip install flask
from flask import Flask 
from flask import (render_template,
    request, #para recibir la información ingresada a través de los forms
    redirect # para redireccionar la informacion y poder mostrarla
    )
#from googlesearch import search
#from googlesearch.googlesearch import GoogleSearch

from googlesearch import search


app = Flask(__name__)
# mysql = MySQL()

# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# # app.config['MySQL_DATABASE_PORT'] = '3306'
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'escalera'
# app.config['MYSQL_DATABASE_DB'] = 'ES_ALCANCE'
# mysql.init_app(app)


@app.route('/api/procesar', methods=['POST'])
def procesar_datos():
    data = request.json['datos']  # Recibe los datos de la columna desde Google Sheets
    # Procesa los datos y devuelve las respuestas
    respuestas = [tu_funcion(item) for item in data]
    return jsonify({'respuestas': respuestas})

def revisar_index(item):
    # Checar cada url en Google y registrar los resultados

    query = f'site:{item}'
    try:
        search_results = list(search(query))
        results = 1 if any(url in result for result in search_results) else 0
    except Exception as e:
        print(f'Error al buscar {url}. Error {e}')
        results = 0
        time.sleep(1)

    # Aquí puedes colocar la lógica para procesar cada elemento de los datos
    # Retorna la respuesta para un elemento específico
    return results 







if __name__ == '__main__':
    app.run(debug=True)
