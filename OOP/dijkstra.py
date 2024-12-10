from template_graph import Graph
from heapq import heappop, heappush
import sys

def dijkstra(graph, source):
    dist = {node: sys.maxsize for node in graph.nodes}
    dist[source] = 0
    prev = {node: None for node in graph.nodes}
    pq = [(0, source)]

    while pq:
        current_dist, current_node = heappop(pq)
        for neighbor, weight in graph.adj_list[current_node]:
            distance = current_dist + weight
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = current_node
                heappush(pq, (distance, neighbor))

    return dist, prev

if __name__ == '__main__':
    nodes = [0, 1, 2, 3, 4, 5]
    edges = [
        (0, 1, 10), (0, 4, 3), (1, 2, 2), (1, 4, 4),
        (2, 3, 9), (3, 2, 7), (4, 1, 1), (4, 2, 8), (4, 3, 2)
    ]
    graph = Graph(nodes, edges)
    source = 0
    dist, prev = dijkstra(graph, source)
    print("Distancias desde el nodo:", dist)
