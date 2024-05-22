import streamlit as st

import time
from googlesearch import search

# Definir la función para procesar los datos
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

# Definir la interfaz de usuario de Streamlit
def main():
    st.title('Procesamiento de Datos')

    # Obtener el dato de entrada del usuario
    dato = st.text_input('Ingrese el dato:')

    # Procesar el dato y mostrar el resultado
    if st.button('Procesar'):
        resultado = procesar_dato(dato)
        st.write('Resultado:', resultado)

if __name__ == '__main__':
    main()

