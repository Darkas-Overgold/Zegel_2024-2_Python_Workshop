"""
La herencia permite que una clase derive de otra, reutilizando su funcionalidad y extendiéndola. 
A continuación, creamos una subclase WeightedGraph que hereda de Graph pero añade una nueva 
funcionalidad para obtener el peso de una arista específica.
"""
class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.adj_list = {node: [] for node in nodes}
        for src, dest, weight in edges:
            self.adj_list[src].append((dest, weight))

    def display(self):
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {neighbors}")

class WeightedGraph(Graph):
    def __init__(self, nodes, edges):
        super().__init__(nodes, edges)  # Llama al constructor de la clase base Graph

    def get_edge_weight(self, src, dest):
        """Devuelve el peso de una arista entre src y dest."""
        for neighbor, weight in self.adj_list.get(src, []):
            if neighbor == dest:
                return weight
        return None  # Si no existe la arista

# Uso
edges = [("A", "B", 1), ("B", "C", 2), ("A", "C", 3)]
graph = WeightedGraph(["A", "B", "C"], edges)
print(graph.get_edge_weight("A", "C"))  # Devuelve 3
