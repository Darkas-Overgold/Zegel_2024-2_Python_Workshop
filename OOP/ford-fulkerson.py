from collections import deque
from template_graph import Graph  # Importa la clase Graph desde el template genérico

def bfs_for_ford_fulkerson(graph, source, sink, parent):
    """
    Realiza una búsqueda BFS para encontrar un camino desde la fuente al sumidero.
    :param graph: Objeto Graph.
    :param source: Nodo fuente.
    :param sink: Nodo sumidero.
    :param parent: Lista para almacenar el camino.
    :return: Verdadero si se encontró un camino, Falso de lo contrario.
    """
    visited = {node: False for node in graph.nodes}
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v, capacity in graph.adj_list[u]:
            if not visited[v] and capacity > 0:  # Si el nodo no está visitado y hay capacidad residual
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == sink:
                    return True
    return False

def ford_fulkerson(graph, source, sink):
    """
    Implementación del algoritmo de Ford-Fulkerson para encontrar el flujo máximo.
    :param graph: Objeto Graph.
    :param source: Nodo fuente.
    :param sink: Nodo sumidero.
    :return: El flujo máximo posible.
    """
    parent = {node: None for node in graph.nodes}
    max_flow = 0

    while bfs_for_ford_fulkerson(graph, source, sink, parent):
        # Encuentra la capacidad de flujo mínima en el camino encontrado
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, dict(graph.adj_list[parent[s]])[s])
            s = parent[s]

        # Actualiza capacidades residuales en las aristas y agrega flujo inverso
        v = sink
        while v != source:
            u = parent[v]
            for i, (adj_node, capacity) in enumerate(graph.adj_list[u]):
                if adj_node == v:
                    graph.adj_list[u][i] = (adj_node, capacity - path_flow)
            for i, (adj_node, capacity) in enumerate(graph.adj_list[v]):
                if adj_node == u:
                    graph.adj_list[v][i] = (adj_node, capacity + path_flow)
            v = parent[v]

        max_flow += path_flow

    return max_flow

if __name__ == '__main__':
    # Lista de nodos
    nodes = [0, 1, 2, 3, 4, 5]
    
    # Lista de aristas en formato (origen, destino, capacidad)
    edges = [
        (0, 1, 16), (0, 2, 13), (1, 2, 10), (1, 3, 12),
        (2, 1, 4), (2, 4, 14), (3, 2, 9), (3, 5, 20),
        (4, 3, 7), (4, 5, 4)
    ]

    # Crear el grafo usando la clase genérica
    graph = Graph(nodes, [(src, dest, capacity) for src, dest, capacity in edges])

    # Define los nodos fuente y sumidero
    source = 0
    sink = 5

    # Ejecuta el algoritmo de Ford-Fulkerson
    max_flow = ford_fulkerson(graph, source, sink)
    print(f"El flujo máximo posible es: {max_flow}")
