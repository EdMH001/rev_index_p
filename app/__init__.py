import streamlit as st
import urllib.parse
import time
from googlesearch import search
# Definir la función de procesamiento de datos
def procesar_dato(dato):
    # Realizar el procesamiento necesario
    # Por ejemplo, simplemente devolver el dato procesado
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

# Definir la ruta de la aplicación para recibir los datos
@st.experimental_memo()
def app():
    # Obtener el dato de la URL
    dato = st.experimental_get_query_params().get("dato", "")
    
    # Procesar el dato
    resultado = procesar_dato(dato)
    
    # Devolver el resultado
    return resultado

# Ejecutar la aplicación
if __name__ == "__main__":
    resultado = app()
    st.write(resultado)







