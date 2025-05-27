'''
1. Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
'''


def calcular_factorial(num):
    if num == 1:
        return 1
    return num * calcular_factorial(num - 1)


def ejercicio_01():
    num = int(input("Ingrese un número: "))
    print(calcular_factorial(num))


'''
2. Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
'''


def fibonacci(posicion):
    if posicion == 0:
        return 0
    if posicion == 1:
        return 1
    return fibonacci(posicion - 1) + fibonacci(posicion - 2)


def ejercicio_02():
    num = int(input("Ingrese un número: "))
    print(
        f"para la posicion {num}, el valor de fibonacci es: {fibonacci(num)}")


'''
3. Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛^𝑚 = (𝑛 ∗ 𝑛)^(𝑚−1)
. Prueba esta función en un
algoritmo general.

'''


def calcular_exponente(base, exponente):
    if exponente == 0:
        return 1
    return base * calcular_exponente(base, exponente - 1)


def ejercicio_03():
    base = int(input("Ingrese un número para la base: "))
    exponente = int(input("Ingrese un número para el exponente: "))
    print(f"{base}^{exponente} = {calcular_exponente(base, exponente)}")


'''
4. Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

Convertir el número 10 a binario:
10 ÷ 2 = 5 resto: 0
5 ÷ 2 = 2 resto: 1
2 ÷ 2 = 1 resto: 0
1 ÷ 2 = 0 resto: 1
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".
'''


def obtener_digitos(lista_restos, numero):
    if numero == 0:
        lista_restos.append("0")
        return 0
    lista_restos.append(str(numero % 2))
    return obtener_digitos(lista_restos, numero // 2)


def convertir_a_binario(numero):
    lista_restos = []
    obtener_digitos(lista_restos, numero)
    lista_restos.reverse()
    return "".join(lista_restos)


def ejercicio_04():
    numero = int(input("Ingrese un número entero: "))
    print(
        f"El valor binario del numero {numero} es: {convertir_a_binario(numero)}")


'''
5. Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.

Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
'''


def validar_letras(palabra, inicio, fin):
    if (inicio == fin):
        return True
    elif (palabra[inicio] == palabra[fin]):
        return validar_letras(palabra, inicio + 1, fin - 1)
    return False


def es_palindromo(palabra):
    return validar_letras(palabra, 0, len(palabra) - 1)


def ejercicio_05():
    palabra = input("Ingrese una palabra: ")
    print(
        f"La palabra {palabra.lower()} es palíndromo: {es_palindromo(palabra.lower())}")


'''
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.

Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
'''


def suma_digitos(n):
    if n == 0:
        return n
    return (n % 10) + suma_digitos(n // 10)


def ejercicio_06():
    numero = int(input("Ingrese un número para ver la suma de sus digitos: "))
    print(
        f"La suma de los dígitos del número {numero} es {suma_digitos(numero)}")


'''
7. Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)

'''


def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)


def ejercicio_07():
    num1 = int(input("Ingrese la cantidad de bloques de la base: "))

    print(
        f"Para construir una pirámida de {num1} bloques, se necesitan {contar_bloques(num1)} bloques.")


'''
8. Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
contar_digito(123456, 7) → 0

'''


def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)


def ejercicio_08():
    numero = int(input("Ingrese un número entero para validar: "))
    digito = int(
        input("Ingrese un número entero entre 0 y 9 a buscar en el número: "))
    while digito < 0 or digito > 9:
        print("Número incorrecto. Debe ser un entero entre 0 y 9")
        digito = int(
            input("Ingrese un número entero entre 0 y 9 a buscar en el número: "))
    print(
        f"Se encontraron {contar_digito(numero, digito)} coincidencias para el dígito {digito}, en el número {numero}.")


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
print("FIN EJECUCIÓN EJERCICIOS: ----------------------------------------------------------------------------")
