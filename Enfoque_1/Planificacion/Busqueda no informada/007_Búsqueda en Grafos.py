# Grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Búsqueda en Grafos
def busqueda_grafos(grafo, inicio, objetivo):
    visitados = set()
    cola = [inicio]

    while cola:
        nodo = cola.pop(0)

        if nodo == objetivo:
            return True

        if nodo not in visitados:
            visitados.add(nodo)
            cola.extend(grafo.get(nodo, []))

    return False

# Llamamos a la función de búsqueda en grafos
print("¿Hay camino?:", busqueda_grafos(grafo, 'A', 'F'))
