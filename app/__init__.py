from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json  # Obtener los datos enviados desde Google Sheets
    processed_data = []  # Procesa tus datos con tu función de Python
    for item in data:
        # Procesar los datos aquí y agregar los resultados a processed_data
        processed_data.append(item * 2)  # Ejemplo de procesamiento

    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=True)
