"""
El encapsulamiento implica ocultar los detalles internos de un objeto y exponer solo lo necesario mediante métodos públicos. 
A continuación se muestra cómo encapsular la lista de adyacencia para que no sea modificada directamente desde fuera de la 
clase, usando un getter.
"""
class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self._adj_list = {node: [] for node in nodes}  # Lista de adyacencia privada
        for src, dest, weight in edges:
            self._adj_list[src].append((dest, weight))

    def get_adj_list(self):
        """Método para obtener la lista de adyacencia de forma segura."""
        return self._adj_list.copy()  # Retorna una copia para evitar modificaciones directas

    def display(self):
        for node, neighbors in self._adj_list.items():
            print(f"{node}: {neighbors}")

# Uso
graph = Graph(["A", "B", "C"], [("A", "B", 1), ("B", "C", 2)])
print(graph.get_adj_list())  # Acceso seguro a la lista de adyacencia
