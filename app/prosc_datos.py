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
    
    return results
