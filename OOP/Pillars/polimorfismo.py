"""
El polimorfismo permite que objetos de diferentes clases puedan ser tratados de manera uniforme, 
aunque pertenezcan a clases diferentes. Vamos a crear una clase GraphWithDFS que herede de Graph 
y sobreescriba el método display para mostrar el grafo de una manera diferente.

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

class GraphWithDFS(Graph):
    def display(self):
        """Sobrescribe el método display para mostrar el grafo con un recorrido DFS."""
        print("Recorrido DFS:")
        visited = set()

        def dfs(node):
            if node not in visited:
                visited.add(node)
                print(node, end=" -> ")
                for neighbor, _ in self.adj_list[node]:
                    dfs(neighbor)

        # Inicia el DFS desde el primer nodo
        dfs(self.nodes[0])
        print("Fin del recorrido")

# Uso
edges = [("A", "B", 1), ("B", "C", 2), ("A", "C", 3)]
graph = GraphWithDFS(["A", "B", "C"], edges)
graph.display()  # Muestra el recorrido DFS
