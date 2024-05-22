import streamlit as st
from flask import Flask, request, jsonify

# Configuración de Flask
flask_app = Flask(__name__)

@flask_app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json  # Obtener los datos enviados desde Google Sheets
    processed_data = []  # Procesa tus datos con tu función de Python
    for item in data:
        # Procesar los datos aquí y agregar los resultados a processed_data
        processed_data.append(item * 2)  # Ejemplo de procesamiento

    return jsonify(processed_data)

# Configuración de Streamlit
def main():
    st.title('Procesamiento de datos')

    # Obtén los datos ingresados por el usuario
    data = st.text_area("Ingrese los datos aquí (separados por coma)", height=200)

    if st.button("Procesar"):
        # Llama a la función en Flask para procesar los datos
        response = flask_app.test_client().post('/process_data', json=data.split(","))
        processed_data = response.json

        # Muestra los resultados
        st.write("Resultados del procesamiento:")
        st.write(processed_data)

if __name__ == "__main__":
    main()
