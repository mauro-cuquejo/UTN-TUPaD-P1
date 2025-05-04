import random

# se agrega una constante para poder cambiar la cantidad de números a procesar, para poder parametrizar la cantidad de ciclos en los ejercicios 8 y 9.
CANT_NUMEROS = 100

'''
1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range.
'''


def ejercicio_01():
    lista = list(range(0, 101, 4))
    print(lista)


'''
2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!
'''


def ejercicio_02():
    lista = ['mauro', 'estudia', 'programacion', 'en', 'UTN']
    print(lista[-2])


'''
3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo:
lista_vacia = []
'''


def ejercicio_03():
    lista = []
    lista.append("primero")
    lista.append("segundo")
    lista.append("tercero")
    print(lista)


'''
4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
'''


def ejercicio_04():
    animales = ["perro", "gato", "conejo", "pez"]
    animales[2] = "loro"
    animales[-1] = "oso"
    print(animales)


'''
5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
    numeros = [8,15,3,22,7]
    numeros.remove(max(numeros))
    print(numeros)
'''


def ejercicio_05():
    # crea una lista con cinco elementos numéricos
    numeros = [8, 15, 3, 22, 7]
    # Primero, hay que analizar qué devuelve la función max(numeros). Esta retorna el valor mas alto dentro de la lista numeros. En este caso, 22.
    # por lo tanto, la instrucción que se ejecutaría, sería numeros.remove(22) eliminando el valor 22 de la lista
    numeros.remove(max(numeros))
    # se imprime la lista, que deberia ahora ser: [8, 15, 3, 7]
    print(numeros)


'''
6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros.
'''


def ejercicio_06():
    lista = list(range(10, 31, 5))
    print(lista[:2])


'''
7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]

'''


def ejercicio_07():
    autos = ["sedan", "polo", "suran", "gol"]
    autos[1] = "ford"
    autos[2] = "peugeot"
    print(autos)


'''
8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla.
'''


def ejercicio_08(cant_numeros):
    dobles = []
    for i in range(5, 16, 5):
        dobles.append(i * 2)
    print(dobles)


'''
9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

    a) Agregar "jugo" a la lista del tercer cliente usando append.
    b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    c) Eliminar "pan" de la lista del primer cliente.
    d) Imprimir la lista resultante por pantalla
'''


def ejercicio_09(cant_numeros):

    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    compras[2].append("jugo")
    compras[1][1] = "tallarines"
    compras[0].remove("pan")
    print(compras)


'''
10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
    ● Posición lista_anidada[0]: 15
    ● Posición lista_anidada[1]: True
    ● Posición lista_anidada[2][0]: 25.5
    ● Posición lista_anidada[2][1]: 57.9
    ● Posición lista_anidada[2][2]: 30.6
    ● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla.

'''


def ejercicio_10():
    lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
    print(lista_anidada)


print("EJECUCIÓN EJERCICIOS: ----------------------------------------------------------------------------")
print("Ejercicio 1  ----------------------------------------------------------------------------")
ejercicio_01()
print("Ejercicio 2 ----------------------------------------------------------------------------")
ejercicio_02()
print("Ejercicio 3 ----------------------------------------------------------------------------")
ejercicio_03()
print("Ejercicio 4 ----------------------------------------------------------------------------")
ejercicio_04()
print("Ejercicio 5 ----------------------------------------------------------------------------")
ejercicio_05()
print("Ejercicio 6 ----------------------------------------------------------------------------")
ejercicio_06()
print("Ejercicio 7 ----------------------------------------------------------------------------")
ejercicio_07()
print("Ejercicio 8 ----------------------------------------------------------------------------")
ejercicio_08(CANT_NUMEROS)
print("Ejercicio 9 ----------------------------------------------------------------------------")
ejercicio_09(CANT_NUMEROS)
print("Ejercicio 10 ----------------------------------------------------------------------------")
ejercicio_10()
print("FIN EJECUCIÓN EJERCICIOS: ----------------------------------------------------------------------------")
