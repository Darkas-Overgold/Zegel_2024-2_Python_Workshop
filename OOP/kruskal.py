from template_graph import Graph

class DisjointSet:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}

    def find(self, k):
        if self.parent[k] == k:
            return k
        self.parent[k] = self.find(self.parent[k])
        return self.parent[k]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        self.parent[root_a] = root_b

def kruskal(graph):
    edges = [(src, dest, weight) for src, neighbors in graph.adj_list.items() for dest, weight in neighbors]
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(graph.nodes)
    mst = []

    for src, dest, weight in edges:
        if ds.find(src) != ds.find(dest):
            mst.append((src, dest, weight))
            ds.union(src, dest)

    return mst

if __name__ == '__main__':
    nodes = [0, 1, 2, 3, 4, 5, 6]
    edges = [
        (0, 1, 7), (1, 2, 8), (0, 3, 5), (1, 3, 9),
        (1, 4, 7), (2, 4, 5), (3, 4, 15), (3, 5, 6),
        (4, 5, 8), (4, 6, 9), (5, 6, 11)
    ]
    graph = Graph(nodes, edges)
    mst = kruskal(graph)
    print("MST:", mst)
