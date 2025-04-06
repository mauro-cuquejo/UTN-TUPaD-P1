from statistics import mode, median, mean
import random
'''
1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

'''


def ejercicio_01():
    edad = int(input("Ingrese la edad: "))
    # Segun la consigna, debe ser mayor a 18, por eso se utiliza un > y no un >=
    if edad > 18:
        print("Es mayor de edad")

# ejercicio_01()


'''
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.

'''


def ejercicio_02():
    nota = int(input("Ingrese su nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

# ejercicio_02()


'''
3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar.
'''


def ejercicio_03():
    # Se toman ints, pero se podria utilizar un float
    num = int(input("Ingrese un numero par: "))
    if num % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

# ejercicio_03()


'''
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
'''


def ejercicio_04():
    edad = int(input("Ingrese su edad: "))
    # no se solicita, pero agrego validacion para evitar una edad menor a cero
    if edad < 0:
        print("Edad incorrecta")
    elif edad < 12:
        print("Niño")
    elif edad >= 12 and edad < 18:
        print("Adolescente")
    elif edad >= 18 and edad < 30:
        print("Adulto joven")
    else:
        print("Adulto")

# ejercicio_04()


'''
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
'''


def ejercicio_05():
    password = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")

    # para evitar ejecutar la funcion más de una vez se almacena en una variable
    longitud_password = len(password)
    if longitud_password >= 8 and longitud_password <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ejercicio_05()


'''
) El paquete statistics de python contiene funciones que permiten tomar una lista de números
y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
siguiente:
from statistics import mode, median, mean
mi_lista = [1,2,5,5,3]
mean(mi_lista)
En la documentación oficial se puede encontrar más información sobre este paquete:
https://docs.python.org/es/3.8/library/statistics.html.
La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
mediana es mayor que la moda.
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
la mediana es menor que la moda.
● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
forma aleatoria.'''


def ejercicio_06():
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)

    # se imprimen la lista, y los valores de moda, mediana y media, simplemente para poder visualizar mejor si entró bien en las condiciones.
    print(f"Esta es la lista de numeros aleatorios: {numeros_aleatorios}")
    print(f"moda: {moda}")
    print(f"mediana: {mediana}")
    print(f"media: {media}")

    if media > mediana and mediana > moda:
        print("Sesgo positivo o a la derecha")
    elif media < mediana and mediana > moda:
        print("Sesgo negativo o a la izquierda")
    elif media == mediana and mediana == moda:
        print("Sin sesgo")

    # no se tienen en cuenta otros casos, tales como media > mediana and mediana < moda

# ejercicio_06()


'''
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
'''


def ejercicio_07():
    frase = input("Ingrese frase o palabra: ")
    if frase[-1] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        frase += "!"
    print(frase)

# ejercicio_07()


'''
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
'''


def ejercicio_08():
    nombre = input("Ingrese su nombre: ")
    opcion = int(input("Ingrese una opción (1, 2, 3)"))

    if (opcion == 1):
        print(nombre.upper())
    elif (opcion == 2):
        print(nombre.lower())
    elif (opcion == 3):
        print(nombre.title())
    else:
        print("opción incorrecta")

# ejercicio_08()


'''
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
'''


def ejercicio_09():
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    if magnitud < 3.0:
        print("Muy leve")
    elif magnitud >= 3.0 and magnitud < 4.0:
        print("Leve")
    elif magnitud >= 4.0 and magnitud < 5.0:
        print("Moderado")
    elif magnitud >= 5.0 and magnitud < 6.0:
        print("Fuerte")
    elif magnitud >= 6.0 and magnitud < 7.0:
        print("Muy fuerte")
    elif magnitud >= 7.0:
        print("Extremo")


# ejercicio_09()
'''
10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año

__________________________________________________________________________________________________________________________________
|Periodo del año	                                            |Estación en el hemisferio norte	|Estación en el hemisferio sur |
|Desde el 21 de diciembre hasta el 20 de marzo (incluidos)	    |Invierno	                        |Verano                        |
|Desde el 21 de marzo hasta el 20 de junio (incluidos)	        |Primavera	                        |Otoño                         |
|Desde el 21 de junio hasta el 20 de septiembre (incluidos)	    |Verano	                            |Invierno                      |
|Desde el 21 de septiembre hasta el 20 de diciembre (incluidos)	|Otoño	                            |Primavera                     |
___________________________________________________________________________________________________________________________________


Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

'''


def ejercicio_10():
    hemisferio = input("Ingrese hemisferio donde se encuentra (N/S): ")
    dia = int(input("Ingrese día del año: "))
    mes = int(input("Ingrese mes del año: "))

    if (dia >= 21 and mes == 12) or (mes >= 1 and mes <= 2) or (dia <= 20 and mes == 3):
        if (hemisferio == "N"):
            print("Invierno")
        elif (hemisferio == "S"):
            print("Verano")
    elif (dia >= 21 and mes == 3) or (mes >= 4 and mes <= 5) or (dia <= 20 and mes == 6):
        if (hemisferio == "N"):
            print("Primavera")
        elif (hemisferio == "S"):
            print("Otoño")

    elif (dia >= 21 and mes == 6) or (mes >= 7 and mes <= 8) or (dia <= 20 and mes == 9):
        if (hemisferio == "N"):
            print("Verano")
        elif (hemisferio == "S"):
            print("Invierno")

    elif (dia >= 21 and mes == 9) or (mes >= 10 and mes <= 11) or (dia <= 20 and mes == 12):
        if (hemisferio == "N"):
            print("Otoño")
        elif (hemisferio == "S"):
            print("Primavera")


# ejercicio_10()
