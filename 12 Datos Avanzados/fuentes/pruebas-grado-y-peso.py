from auxiliar_pruebas import crear_arbol_para_pruebas, imprimir_arbol_vertical
from arbol_binario import calcular_grado_arbol_post_orden, calcular_peso_post_orden

arbol_nuevo = crear_arbol_para_pruebas(False)

print("-" * 50)
imprimir_arbol_vertical(arbol_nuevo)
print("-" * 50)
print(f"Grado maximo arbol: {calcular_grado_arbol_post_orden(arbol_nuevo)}")
print("-" * 50)
print(f"Peso arbol: {calcular_peso_post_orden(arbol_nuevo)}")
print("-" * 50)
