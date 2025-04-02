import heapq

def astar(graph, start, goal, h):
    priority_queue = [(0, [start])]
    visited = set()
    
    while priority_queue:
        cost, path = heapq.heappop(priority_queue)
        node = path[-1]
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            return path
        
        for neighbor, weight in graph.get(node, []):
            new_path = list(path)
            new_path.append(neighbor)
            new_cost = cost + weight + h(neighbor)
            heapq.heappush(priority_queue, (new_cost, new_path))
    
    return None

# Ejemplo de uso
graph_weighted = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 2)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
h = lambda x: {'A': 6, 'B': 4, 'C': 2, 'D': 3, 'E': 1, 'F': 0}.get(x, 0)
print(astar(graph_weighted, 'A', 'F', h))  # Salida esperada: ['A', 'B', 'E', 'F']
