from auxiliar_pruebas import crear_arbol_para_pruebas, imprimir_arbol_vertical
from arbol_binario import buscar_nodo

arbol_nuevo = crear_arbol_para_pruebas(False)

print("-" * 50)
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
