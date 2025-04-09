import heapq  # Importamos heapq para manejar la cola de prioridad

def busqueda_costo_uniforme(grafo, inicio, objetivo):
    cola_prioridad = []  # Cola de prioridad para los nodos a explorar
    heapq.heappush(cola_prioridad, (0, inicio))  # Insertamos el nodo inicial con costo 0
    costos = {inicio: 0}  # Diccionario para registrar el menor costo a cada nodo
    camino = {}  #camino óptimo

    while cola_prioridad: #Mientras haya nodos por explorar
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)  #nodo con menor costo

        if nodo_actual == objetivo: 
            break

        for vecino, costo in grafo[nodo_actual]:  # Recorremos los vecinos y sus costos
            nuevo_costo = costo_actual + costo  # Calculamos el costo acumulado

            if vecino not in costos or nuevo_costo < costos[vecino]:  
                costos[vecino] = nuevo_costo  # Guardamos el menor costo encontrado
                heapq.heappush(cola_prioridad, (nuevo_costo, vecino))  # Lo agregamos a la cola
                camino[vecino] = nodo_actual  # Guardamos el nodo previo en el camino

    # Reconstruimos el camino óptimo desde el objetivo hasta el inicio
    nodo = objetivo
    ruta = []
    while nodo in camino:
        ruta.append(nodo)
        nodo = camino[nodo]
    ruta.append(inicio)
    ruta.reverse()  # Invertimos la lista para mostrarla en orden correcto

    print("Mejor ruta:", " -> ".join(ruta))
    print("Costo total:", costos[objetivo])

# Grafo con pesos (costo entre nodos)
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

# Llamamos a la función UCS desde A hasta F
busqueda_costo_uniforme(grafo, 'A', 'F')
