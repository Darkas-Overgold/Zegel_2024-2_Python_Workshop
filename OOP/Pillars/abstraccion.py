"""
La abstracción implica ocultar la complejidad del sistema y proporcionar una interfaz sencilla. 
Vamos a agregar un método que abstrae la lógica de agregar una arista al grafo, simplificando la interacción del usuario.
"""
class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.adj_list = {node: [] for node in nodes}
        for src, dest, weight in edges:
            self.adj_list[src].append((dest, weight))

    def add_edge(self, src, dest, weight):
        """Abstracción para agregar una arista al grafo."""
        if src in self.adj_list and dest in self.adj_list:
            self.adj_list[src].append((dest, weight))
        else:
            print("Error: uno o ambos nodos no existen en el grafo.")

    def display(self):
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {neighbors}")

# Uso
graph = Graph(["A", "B", "C"], [("A", "B", 1), ("B", "C", 2)])
graph.add_edge("A", "C", 3)  # Añade una nueva arista
graph.display()
