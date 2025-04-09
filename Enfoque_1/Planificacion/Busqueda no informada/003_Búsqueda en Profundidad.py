def busqueda_profundidad(grafo, inicio, objetivo, visitados=None):
    if visitados is None:
        visitados = set()
    
    visitados.add(inicio)
    if inicio == objetivo:
        return [inicio]

    for vecino in grafo[inicio]:
        if vecino not in visitados:
            camino = busqueda_profundidad(grafo, vecino, objetivo, visitados)
            if camino:
                return [inicio] + camino
    
    return None

# Grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Llamamos a la función DFS desde A hasta F
print("Ruta encontrada:", busqueda_profundidad(grafo, 'A', 'F'))
