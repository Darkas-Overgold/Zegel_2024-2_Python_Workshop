#Programación Cuántica
import networkx as nx
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Definir un grafo clásico
def crear_grafo():
    grafo = nx.Graph()
    grafo.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)])  # Conexiones entre nodos
    return grafo

# Crear un circuito cuántico basado en el grafo
def grafo_cuantico(grafo, num_qubits):
    # Crear un circuito con un número de qubits igual al número de nodos
    circuito = QuantumCircuit(num_qubits)

    # Inicializar cada nodo en superposición
    for nodo in grafo.nodes:
        circuito.h(nodo)  # Puerta Hadamard para superposición

    # Agregar las conexiones (aristas) como puertas CNOT
    for nodo1, nodo2 in grafo.edges:
        circuito.cx(nodo1, nodo2)

    return circuito

# Simular el circuito
def simular_circuito(circuito):
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuito, backend, shots=1024)
    resultados = job.result().get_counts()
    return resultados

# Graficar los resultados
def graficar_resultados(resultados):
    plot_histogram(resultados)
    plt.show()

# Graficar el grafo clásico
def graficar_grafo(grafo):
    pos = nx.circular_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', font_weight='bold')
    plt.title("Grafo Clásico")
    plt.show()

# Programa principal
if __name__ == "__main__":
    # Crear y mostrar el grafo clásico
    grafo = crear_grafo()
    graficar_grafo(grafo)

    # Crear un circuito cuántico basado en el grafo
    circuito = grafo_cuantico(grafo, num_qubits=len(grafo.nodes))
    print(circuito)

    # Simular el circuito cuántico
    resultados = simular_circuito(circuito)
    print("Resultados de la simulación:", resultados)

    # Mostrar el histograma de resultados
    graficar_resultados(resultados)