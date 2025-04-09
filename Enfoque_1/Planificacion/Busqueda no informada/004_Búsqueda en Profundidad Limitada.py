# Grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Búsqueda en Profundidad Limitada
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

# Llamamos a la función con un límite de 2 niveles
print("Ruta encontrada:", busqueda_profundidad_limitada(grafo, 'A', 'F', 2))
