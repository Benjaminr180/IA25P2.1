# Grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Búsqueda en Profundidad Limitada (como función auxiliar)
def busqueda_profundidad_limitada(grafo, inicio, objetivo, limite, profundidad=0):
    if inicio == objetivo:
        return [inicio]

    if profundidad >= limite:
        return None

    for vecino in grafo[inicio]:
        camino = busqueda_profundidad_limitada(grafo, vecino, objetivo, limite, profundidad + 1)
        if camino:
            return [inicio] + camino

    return None

# Búsqueda en Profundidad Iterativa
def busqueda_profundidad_iterativa(grafo, inicio, objetivo, profundidad_maxima):
    for limite in range(profundidad_maxima + 1):
        resultado = busqueda_profundidad_limitada(grafo, inicio, objetivo, limite)
        if resultado:
            return resultado
    return None

# Llamamos a la función con profundidad máxima de 3
print("Ruta encontrada:", busqueda_profundidad_iterativa(grafo, 'A', 'F', 3))
