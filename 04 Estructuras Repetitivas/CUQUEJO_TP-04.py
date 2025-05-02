import random

'''1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
    (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.'''


def ejercicio_01():
    for i in range(1, 101):
        print(i)


'''2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene.'''


def ejercicio_02():
    num = int(input("Ingrese un número entero: "))
    cont = 0
    for i in range(len(str(num))):
        cont += 1
    print(f"El número contiene {cont} dígitos")


'''3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.'''


def ejercicio_03():
    num = int(input("Ingrese un número entero: "))
    num2 = int(input("Ingrese otro número entero: "))
    suma = 0
    if (num < num2):
        for i in range(num + 1, num2):
            suma += i
    else:
        for i in range(num2 + 1, num):
            suma += i
    print(f"la suma de los numeros es: {suma}")


'''4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.'''


def ejercicio_04():
    CERO = 0
    num = int(
        input("Ingrese un número entero distinto de 0. Ingrese 0 para terminar: "))
    suma = 0
    while num != CERO:
        suma += num
        num = int(
            input("Ingrese un número entero distinto de 0. Ingrese 0 para terminar: "))
    print(f"La suma de los números es: {suma}")


'''5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número'''


def ejercicio_05():
    num_aleatorio = random.randint(0, 9)
    intentos = 0
    numero_elegido = 10
    while numero_elegido != num_aleatorio:
        intentos += 1
        numero_elegido = int(
            input("Ingrese un número entero de 0 a 9: "))
        if numero_elegido < 0 or numero_elegido > 10:
            print("El número elegido debe ser entre 0 y 9.")
        elif (numero_elegido != num_aleatorio):
            print("Número incorrecto. Intentá otra vez...")

    print(
        f"Ganaste. el número era: {num_aleatorio} Número de intentos: {intentos}")


'''6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente.
'''


def ejercicio_06():
    print("Los numeros pares del 100 al 0 son: ")
    for i in range(100, 0, -2):
        print(i)


'''7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.'''


def ejercicio_07():
    num = int(input("Ingrese un numero entero positivo: "))
    if (num <= 0):
        print("El numero ingresado debe ser mayor a 0")
    else:
        suma = 0
        for i in range(num):
            suma += i
        print(f"La suma de los números es: {suma}")


'''8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).'''


def ejercicio_08():
    CANT_NUMEROS = 5
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    for i in range(CANT_NUMEROS):
        num = int(input("ingrese un numero: "))
        if (num < 0):
            negativos += 1
        elif (num > 0):
            positivos += 1

        if (num % 2 == 0):
            pares += 1
        else:
            impares += 1
    print(
        f"Positivos: {positivos}, negativos: {negativos}, pares: {pares}, impares: {impares}")


'''9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).'''


def ejercicio_09():
    CANT_NUMEROS = 11
    suma = 0
    for i in range(1, CANT_NUMEROS):
        numero = int(input("Ingrese un número: "))
        suma += numero
    promedio = suma / CANT_NUMEROS
    print(f"El promedio de los números ingresados es: {promedio}")


'''10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.'''


def ejercicio_10():
    numero = input("Ingrese un número: ")
    numero_invertido = ""
    for i in range(len(numero) - 1, -1, -1):
        numero_invertido += numero[i]
    print(f"El valor invertido del número {numero}, es: {numero_invertido}")


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
ejercicio_08()
print("Ejercicio 9 ----------------------------------------------------------------------------")
ejercicio_09()
print("Ejercicio 10 ----------------------------------------------------------------------------")
ejercicio_10()
print("FIN EJECUCIÓN EJERCICIOS: ----------------------------------------------------------------------------")
