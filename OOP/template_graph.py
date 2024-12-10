class Graph:
    def __init__(self, nodes, edges):
        """
        Inicializa un grafo con nodos y aristas.
        :param nodes: Lista de nodos
        :param edges: Lista de tuplas (origen, destino, peso)
        """
        self.nodes = nodes
        self.adj_list = {node: [] for node in nodes}
        for src, dest, weight in edges:
            self.adj_list[src].append((dest, weight))
            # Descomenta la siguiente línea si el grafo es no dirigido
            # self.adj_list[dest].append((src, weight))

    def display(self):
        """Imprime la lista de adyacencia del grafo."""
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {neighbors}")
