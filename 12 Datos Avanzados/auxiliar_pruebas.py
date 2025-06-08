from arbol_binario import crear_nodo, agregar_nodo


def crear_arbol_para_pruebas(imprimir_contenido):
    arbol = crear_nodo()
    arbol["dato"] = 1
    if imprimir_contenido:
        print("-" * 50)
        print(f"creo el arbol de cero: {arbol}")
        imprimir_arbol_vertical(arbol)

        print("-" * 50)
    nodo_nuevo = crear_nodo(2)
    agregar_nodo(arbol, nodo_nuevo)
    if imprimir_contenido:
        print(f"creo el nodo con dato 2: {nodo_nuevo}")
        print("agrego el nodo al arbol:")
        imprimir_arbol_vertical(arbol)

        print("-" * 50)
    nodo_nuevo = crear_nodo(0)
    if imprimir_contenido:
        print(f"creo el nodo con dato 0: {nodo_nuevo}")
    agregar_nodo(arbol, nodo_nuevo)
    if imprimir_contenido:
        print("agrego el nodo al arbol:")
        imprimir_arbol_vertical(arbol)

        print("-" * 50)
    nodo_nuevo = crear_nodo(3)
    if imprimir_contenido:
        print(f"creo el nodo con dato 3: {nodo_nuevo}")
    agregar_nodo(arbol, nodo_nuevo)
    if imprimir_contenido:
        print("agrego el nodo al arbol:")
        imprimir_arbol_vertical(arbol)

        print("-" * 50)
    nodo_nuevo = crear_nodo(-2)
    if imprimir_contenido:
        print(f"creo el nodo con dato -2: {nodo_nuevo}")
    agregar_nodo(arbol, nodo_nuevo)
    if imprimir_contenido:
        print("agrego el nodo al arbol:")
        imprimir_arbol_vertical(arbol)

        print("-" * 50)
    nodo_nuevo = crear_nodo(-1)
    if imprimir_contenido:
        print(f"creo el nodo con dato -1: {nodo_nuevo}")
    agregar_nodo(arbol, nodo_nuevo)
    if imprimir_contenido:
        print("agrego el nodo al arbol:")
        imprimir_arbol_vertical(arbol)

        print("-" * 50)
    nodo_nuevo = crear_nodo(-3)
    if imprimir_contenido:
        print(f"creo el nodo con dato -3: {nodo_nuevo}")
    agregar_nodo(arbol, nodo_nuevo)
    if imprimir_contenido:
        print("agrego el nodo al arbol:")
        imprimir_arbol_vertical(arbol)

        print("-" * 50)
    nodo_nuevo = crear_nodo(4)
    if imprimir_contenido:
        print(f"creo el nodo con dato 4: {nodo_nuevo}")
    agregar_nodo(arbol, nodo_nuevo)
    if imprimir_contenido:
        print("agrego el nodo al arbol:")
        imprimir_arbol_vertical(arbol)
        print("-" * 50)

    if imprimir_contenido:
        nodo_nuevo = crear_nodo(4)
        print(f"creo el nodo con dato 4 (repetido): {nodo_nuevo}")
        agregar_nodo(arbol, nodo_nuevo)
        print("agrego el nodo al arbol (Debe fallar):")
        imprimir_arbol_vertical(arbol)
        print("-" * 50)
    return arbol

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ANEXO: IMPRIMIR ARBOL VISUALMENTE
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
