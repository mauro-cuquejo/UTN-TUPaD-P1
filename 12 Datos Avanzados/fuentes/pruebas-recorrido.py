
from auxiliar_pruebas import crear_arbol_para_pruebas, imprimir_arbol_vertical
from arbol_binario import leer_arbol_pre_orden, leer_arbol_in_orden, leer_arbol_post_orden

arbol_nuevo = crear_arbol_para_pruebas(False)

print("-" * 50)
imprimir_arbol_vertical(arbol_nuevo)
print("-" * 50)
print("Procedo a recorrer el arbol y sus datos en los distintos órdenes:")
print("-" * 50)
print("PREORDEN")
print(leer_arbol_pre_orden(arbol_nuevo))
print("-" * 50)
print("INORDEN")
print(leer_arbol_in_orden(arbol_nuevo))
print("-" * 50)
print("POSTORDEN")
print(leer_arbol_post_orden(arbol_nuevo))
print("-" * 50)
