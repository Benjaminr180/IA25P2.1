# Grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Búsqueda Bidireccional
def busqueda_bidireccional(grafo, inicio, objetivo):
    # Función auxiliar para la búsqueda en un solo lado
    def busqueda_unilateral(grafo, inicio, objetivo):
        visitados = set()
        cola = [[inicio]]

        while cola:
            camino = cola.pop(0)
            nodo = camino[-1]

            if nodo == objetivo:
                return camino

            if nodo not in visitados:
                visitados.add(nodo)
                for vecino in grafo[nodo]:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    cola.append(nuevo_camino)

        return None

    # Buscar desde el inicio y desde el objetivo
    camino_inicio = busqueda_unilateral(grafo, inicio, objetivo)
    camino_objetivo = busqueda_unilateral(grafo, objetivo, inicio)

    if camino_inicio and camino_objetivo:
        # Si encontramos caminos desde ambos extremos, combinamos los caminos
        camino_objetivo.reverse()  # Invertimos el camino desde el objetivo
        return camino_inicio + camino_objetivo[1:]  # Combinamos ambos caminos

    return None

# Llamamos a la función de búsqueda bidireccional
print("Ruta encontrada:", busqueda_bidireccional(grafo, 'A', 'F'))
