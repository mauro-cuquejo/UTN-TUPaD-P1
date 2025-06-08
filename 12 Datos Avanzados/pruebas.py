from arbol_binario import crear_nodo, agregar_nodo, leer_arbol_in_orden, leer_arbol_post_orden, leer_arbol_pre_orden
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
print("Procedo a recorrer el arbol y sus datoes:")
print("PREORDEN")
leer_arbol_pre_orden(arbol_nuevo)
print("INORDEN")
leer_arbol_in_orden(arbol_nuevo)
print("POSTORDEN")
leer_arbol_post_orden(arbol_nuevo)


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FIN PRUEBAS
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ALGUNAS FUNCIONES INTERESANTES PARA VISUALIZAR EL ARBOL:
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# IMPRIMIR EL ARBOL POR NIVELES
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------


def imprimir_por_niveles(arbol):
    if arbol is None:
        return

    cola = deque()
    cola.append((arbol, 0))  # (nodo, nivel)
    nivel_actual = 0
    linea = []

    while cola:
        nodo, nivel = cola.popleft()

        if nivel != nivel_actual:
            print(f"nivel {nivel_actual}: {' '.join(map(str, linea))}")
            linea = []
            nivel_actual = nivel

        linea.append(nodo["dato"])

        if nodo["nodo_izq"]:
            cola.append((nodo["nodo_izq"], nivel + 1))
        if nodo["nodo_der"]:
            cola.append((nodo["nodo_der"], nivel + 1))

    # Imprimir último nivel
    print(f"nivel {nivel_actual}: {' '.join(map(str, linea))}")


print("-" * 50)
print("Recorrido por niveles:")
imprimir_por_niveles(arbol_nuevo)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# IMPRIMIR ARBOL VISUAL (VERSION 1)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------


def imprimir_arbol_formato(arbol, nivel=0, prefijo="Raíz: "):
    if arbol is None:
        return

    imprimir_arbol_formato(arbol["nodo_der"], nivel + 1, "Der: ")

    print("    " * nivel + prefijo + str(arbol["dato"]))

    imprimir_arbol_formato(arbol["nodo_izq"], nivel + 1, "Izq: ")


print("-" * 50)
print("Visualización tipo árbol:")
imprimir_arbol_formato(arbol_nuevo)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# IMPRIMIR ARBOL VISUALMENTE
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------


def imprimir_arbol_vertical(arbol, prefijo="", es_izq=True):
    if arbol is None:
        return

    if arbol["nodo_der"]:
        nuevo_prefijo = prefijo + ("│   " if es_izq else "    ")
        imprimir_arbol_vertical(arbol["nodo_der"], nuevo_prefijo, False)

    print(prefijo + ("└── " if es_izq else "┌── ") + str(arbol["dato"]))

    if arbol["nodo_izq"]:
        nuevo_prefijo = prefijo + ("    " if es_izq else "│   ")
        imprimir_arbol_vertical(arbol["nodo_izq"], nuevo_prefijo, True)


print("-" * 50)
print("Árbol vertical:")
imprimir_arbol_vertical(arbol_nuevo)
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FIN
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
