import sys

# Función para encontrar el nodo con la distancia mínima
def nodo_con_distancia_minima(distancias, visitados):
    min_distancia = sys.maxsize
    min_nodo = None
    for nodo in distancias:
        if distancias[nodo] < min_distancia and not visitados[nodo]:
            min_distancia = distancias[nodo]
            min_nodo = nodo
    return min_nodo

# Función para mostrar el proceso paso a paso
def mostrar_proceso_paso_a_paso(grafo, padres, distancias, visitados, nodo_actual):
    print("Nodo actual:", nodo_actual)
    print("Distancias mínimas:", distancias)
    print("Padres:", padres)
    print("Nodos visitados:", visitados)
    print("")

# Función principal de Prim
def prim(grafo):
    nodos = list(grafo.keys())
    distancias = {nodo: sys.maxsize for nodo in nodos}
    padres = {nodo: None for nodo in nodos}
    visitados = {nodo: False for nodo in nodos}
    
    nodo_inicio = nodos[0]
    distancias[nodo_inicio] = 0

    for _ in nodos:
        nodo_actual = nodo_con_distancia_minima(distancias, visitados)
        if nodo_actual is None:
            break
        visitados[nodo_actual] = True

        for vecino, peso in grafo[nodo_actual].items():
            if not visitados[vecino] and peso < distancias[vecino]:
                distancias[vecino] = peso
                padres[vecino] = nodo_actual

        # Muestra el progreso en la consola
        mostrar_proceso_paso_a_paso(grafo, padres, distancias, visitados, nodo_actual)

    # Construye el Árbol Parcial Mínimo resultante
    arbol_par_minimo = {nodo: {} for nodo in nodos}
    for nodo, padre in padres.items():
        if padre is not None:
            peso = grafo[nodo][padre]
            arbol_par_minimo[nodo][padre] = peso
            arbol_par_minimo[padre][nodo] = peso

    return arbol_par_minimo

# Grafo de ejemplo (representado como un diccionario de diccionarios)
grafo = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 4, 'D': 1},
    'C': {'A': 3, 'B': 4, 'D': 5},
    'D': {'B': 1, 'C': 5}
}

print("Ejecutando el algoritmo de Prim paso a paso:\n")
arbol_par_minimo = prim(grafo)

print("\nÁrbol Parcial Mínimo resultante:")
print(arbol_par_minimo)
