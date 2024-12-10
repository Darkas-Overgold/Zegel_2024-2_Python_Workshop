import networkx as nx

# Algoritmos disponibles en el gestor
algoritmos_grafos = {
    "BFS": "Recorrido en amplitud (Breadth-First Search)",
    "DFS": "Recorrido en profundidad (Depth-First Search)",
    "Dijkstra": "Algoritmo de Dijkstra para caminos más cortos",
    "Kruskal": "Algoritmo de Kruskal para árbol de expansión mínima",
    "Prim": "Algoritmo de Prim para árbol de expansión mínima"
}

def mostrar_algoritmos():
    """Muestra los algoritmos de grafos disponibles."""
    print("\nAlgoritmos de grafos disponibles:")
    for nombre, descripcion in algoritmos_grafos.items():
        print(f"- {nombre}: {descripcion}")

def ejecutar_algoritmo(algoritmo):
    """Ejecuta el algoritmo seleccionado en un grafo de ejemplo."""
    G = nx.Graph()
    G.add_weighted_edges_from([
        (1, 2, 4), (1, 3, 2), (2, 3, 5), (2, 4, 10),
        (3, 4, 3), (3, 5, 6), (4, 5, 1)
    ])
    
    print("\nEjecutando el algoritmo seleccionado...")
    
    if algoritmo == "BFS":
        inicio = int(input("Nodo inicial para BFS: "))
        recorrido = list(nx.bfs_tree(G, source=inicio).nodes)
        print(f"Recorrido BFS desde el nodo {inicio}: {recorrido}")
    elif algoritmo == "DFS":
        inicio = int(input("Nodo inicial para DFS: "))
        recorrido = list(nx.dfs_tree(G, source=inicio).nodes)
        print(f"Recorrido DFS desde el nodo {inicio}: {recorrido}")
    elif algoritmo == "Dijkstra":
        inicio = int(input("Nodo inicial para Dijkstra: "))
        caminos_mas_cortos = nx.single_source_dijkstra_path_length(G, source=inicio)
        print(f"Distancias más cortas desde el nodo {inicio}: {caminos_mas_cortos}")
    elif algoritmo == "Kruskal":
        mst = nx.minimum_spanning_tree(G, algorithm="kruskal")
        print("Árbol de expansión mínima (Kruskal):")
        print(mst.edges(data=True))
    elif algoritmo == "Prim":
        mst = nx.minimum_spanning_tree(G, algorithm="prim")
        print("Árbol de expansión mínima (Prim):")
        print(mst.edges(data=True))
    else:
        print("Algoritmo no reconocido.")

def gestor_grafos():
    """Función principal del gestor de algoritmos de grafos."""
    while True:
        print("\n" + "=" * 40)
        print("Gestor de Algoritmos de Grafos".center(40))
        print("=" * 40)
        print("1. Mostrar algoritmos disponibles")
        print("2. Ejecutar un algoritmo")
        print("3. Salir")
        print("=" * 40)

        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                mostrar_algoritmos()
            elif opcion == "2":
                mostrar_algoritmos()
                algoritmo = input("Introduce el nombre del algoritmo: ")
                if algoritmo in algoritmos_grafos:
                    ejecutar_algoritmo(algoritmo)
                else:
                    print("Error: Algoritmo no válido. Intenta nuevamente.")
            elif opcion == "3":
                print("¡Gracias por usar el gestor! Hasta pronto.")
                break
            else:
                print("Opción no válida. Intenta nuevamente.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

# Ejecutar el programa
gestor_grafos()
