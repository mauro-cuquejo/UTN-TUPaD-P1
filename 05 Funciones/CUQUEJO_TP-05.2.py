from math import pi

# se agrega una constante para poder cambiar la cantidad de números a procesar, para poder parametrizar la cantidad de ciclos en los ejercicios 8 y 9.
CANT_NUMEROS = 100

'''
1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
'''


def imprimir_hola_mundo():
    print("Hola Mundo!")


def ejercicio_01():
    imprimir_hola_mundo()


'''
2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
'''


def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


def ejercicio_02():
    nombre = input("Ingrese su nombre: ")
    saludar_usuario(nombre)


'''
3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

'''


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


def ejercicio_03():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)


'''
4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro
y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio
como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y
llamar ambas funciones para mostrar los resultados.

'''


def calcular_area_circulo(radio):
    return pi * radio ** 2


def calcular_perimetro_circulo(radio):
    return 2 * pi * radio


def ejercicio_04():
    radio = float(input("Ingrese el radio del circulo en cm: "))
    print(f"El área del circulo es de: {calcular_area_circulo(radio)} cm")
    print(
        f"El perímetro del circulo es de: {calcular_perimetro_circulo(radio)} cm")


'''
5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
'''


def segundos_a_horas(segundos):
    return segundos / 3600


def ejercicio_05():
    segundos = float(input("Ingrese la cantidad de segundos: "))
    print(
        f"La cantidad de horas para los segundos ingresados, es de: {segundos_a_horas(segundos)} horas")


'''
6) Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
'''


def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def ejercicio_06():
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)


'''
7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

'''


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return (suma, resta, multiplicacion, division)


def ejercicio_07():
    num1 = float(input("Ingrese un número: "))
    num2 = float(input("Ingrese otro número: "))

    resultado = operaciones_basicas(num1, num2)

    print(f"El resultado de la suma es: {resultado[0]}")
    print(f"El resultado de la resta es: {resultado[1]}")
    print(f"El resultado de la multiplicación es: {resultado[2]}")
    print(
        f"El resultado de la división es: {resultado[3] if resultado[3] != None else 'No se puede dividir por cero'}")


'''
8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

'''


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def ejercicio_08(cant_numeros):
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    print(f"Su Índice de Masa Corporal es de: {calcular_imc(peso, altura)}")


'''
9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.

'''


def celsius_a_fahrenheit(celsius):
    return (9/5) * celsius + 32


def ejercicio_09(cant_numeros):

    temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    print(
        f"La temperatura en grados Farenheit es de: {celsius_a_fahrenheit(temp_celsius)} °F")


'''
10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.

'''


def calcular_promedio(a, b, c):
    return (a + b + c) / 3


def ejercicio_10():
    num1 = float(input("ingrese el primer número: "))
    num2 = float(input("ingrese el segundo número: "))
    num3 = float(input("ingrese el tercer número: "))
    print(
        f"El promedio de los tres números ingresados es de: {calcular_promedio(num1, num2, num3)}")


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
