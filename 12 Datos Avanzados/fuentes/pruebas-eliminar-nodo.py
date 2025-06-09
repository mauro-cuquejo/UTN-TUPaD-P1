from auxiliar_pruebas import crear_arbol_para_pruebas, imprimir_arbol_vertical
from arbol_binario import eliminar_nodo

arbol_nuevo = crear_arbol_para_pruebas(False)

print("-" * 50)
print("arbol inicial:")
imprimir_arbol_vertical(arbol_nuevo)
print("-" * 50)
print("Procedo a eliminar nodos del arbol:")
print("Elimino el nodo 8 (no existe):")
arbol_nuevo = eliminar_nodo(arbol_nuevo, 8)
imprimir_arbol_vertical(arbol_nuevo)

print("-" * 50)
print("Elimino el nodo 4 (sin hijos):")
arbol_nuevo = eliminar_nodo(arbol_nuevo, 4)
imprimir_arbol_vertical(arbol_nuevo)

print("-" * 50)
print("Elimino el nodo 2 (con un hijo):")
arbol_nuevo = eliminar_nodo(arbol_nuevo, 2)
imprimir_arbol_vertical(arbol_nuevo)

print("-" * 50)
print("Elimino el nodo -2 (con dos hijos):")
arbol_nuevo = eliminar_nodo(arbol_nuevo, -2)
imprimir_arbol_vertical(arbol_nuevo)
print("-" * 50)
