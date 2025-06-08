from arbol_binario import crear_nodo, agregar_nodo, leer_arbol_in_orden, leer_arbol_post_orden, leer_arbol_pre_orden, imprimir_arbol_vertical, calcular_arbol_post_orden, calcular_peso_post_orden, buscar_nodo
from collections import deque
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# PRUEBAS:
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
arbol_nuevo = crear_nodo()

arbol_nuevo["dato"] = 1
print(f"creo el arbol de cero: {arbol_nuevo}")
print("-" * 50)
nodo_nuevo = crear_nodo(2)
agregar_nodo(arbol_nuevo, nodo_nuevo)
print(f"creo el nodo con dato 2: {nodo_nuevo}")
print(f"agrego el nodo al arbol: {arbol_nuevo}")
print("-" * 50)
print("Procedo a recorrer el arbol y sus datos:")
print("PREORDEN")
leer_arbol_pre_orden(arbol_nuevo)
print("INORDEN")
leer_arbol_in_orden(arbol_nuevo)
print("POSTORDEN")
leer_arbol_post_orden(arbol_nuevo)
print("-" * 50)
nodo_nuevo = crear_nodo(0)
print(f"creo el nodo con dato 0: {nodo_nuevo}")
agregar_nodo(arbol_nuevo, nodo_nuevo)

nodo_nuevo = crear_nodo(3)
print(f"creo el nodo con dato 3: {nodo_nuevo}")
agregar_nodo(arbol_nuevo, nodo_nuevo)

print(f"agrego ambos nodos al arbol: {arbol_nuevo}")
print("-" * 50)
print("Procedo a recorrer el arbol y sus datos:")
print("PREORDEN")
leer_arbol_pre_orden(arbol_nuevo)
print("INORDEN")
leer_arbol_in_orden(arbol_nuevo)
print("POSTORDEN")
leer_arbol_post_orden(arbol_nuevo)

print("-" * 50)
print("Árbol vertical:")
imprimir_arbol_vertical(arbol_nuevo)
print("-" * 50)
print("Busco el nodo de valor 3 e imprimo el subarbol obtenido:")
nodo3 = buscar_nodo(arbol_nuevo, 3)
imprimir_arbol_vertical(nodo3)
print("-" * 50)
print("Busco el nodo de valor 2 e imprimo el subarbol obtenido:")
nodo2 = buscar_nodo(arbol_nuevo, 2)
imprimir_arbol_vertical(nodo2)

print("-" * 50)
print(f"Grado maximo arbol: {calcular_arbol_post_orden(arbol_nuevo)}")
print("-" * 50)
print(f"Peso arbol: {calcular_peso_post_orden(arbol_nuevo)}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FIN PRUEBAS
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FIN
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
