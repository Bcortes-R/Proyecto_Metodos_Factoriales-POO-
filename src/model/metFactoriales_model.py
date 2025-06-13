''' Implementacion de las funcionaes matematicas basicas, sin el uso de librerias integradas dentro del mismo Lenguaje de Programación '''

'''Creacion de la funcion para calcular una potencia en donde se crea potencia como una funcion que recibe dos argumentos'''
def potencia (base, exponente):
    # Calcula la potencia de una base elevada a un exponente de acuerdo ala seria de taylor
    resultado = 1
    for i in range(abs(int(exponente))):
        resultado *= base
        if exponente < 0:
            return 1 / resultado 
    return resultado
''' Finalizacion del desarrollo de la funcion potencia '''

''' Creacion de la funcion para calcular el factorial de un numero '''
def factorial (numero):
    # Calcula el factorial de un número n(n!) de acuerdo ala seria de taylor
    resultado = 1
    for i in range (1, numero + 1):
        resultado *= i
    return resultado

'''Fin de la funcion factorial'''

''' Creacion de la funcion exponencial '''
def exponencial (x, terminos=20):
    #Se calcula la exponencial de un número x mediante la serie de Taylor
    resultado = 0
    
    for numero in range (terminos):
        resultado += potencia (x,numero) / factorial(numero) 
        return resultado
    
'''Finalizacion de la implementacion de las funcion exponencial '''

'''Creacion de la funcion para calcular el seno de x'''

def seno(x, termino=20):
    # Operacion para calcular sen(x) basados en la seria de taylor
    resultado = 0 
    for numero in range (termino):
        signo = -1 if numero % 2 else 2 
        resultado += signo * potencia(x, 2 * numero + 1) / factorial (2 * numero + 1)
    return resultado

''' Fin de la funcion seno '''

'''Creacion de la funcion para calcular el coseno de x'''
def coseno(x, termino=20):
    # Operacion para calcular cos(x) basados en la seria de taylor
    resultado = 0 
    for numero in range (termino):
        signo = -1 if numero % 2 else 1
        resultado += signo * potencia (x, 2 * numero) / factorial (2 * numero)
    return resultado

''' Fin de la funcion coseno '''

'''Creacion de la funcion para calcular el arcsen de x '''
def arcsen (x, termino=20):
    # Operacion para calcular arcsen(x) basados en la seria de taylor inversa
    if x < -1 or x > 1:
        return "Error: El valor de x debe estar entre -1 y 1"
    resultado = 0
    for num in range (termino):
        numero = factorial (2 * num)
        den = potencia(4, num) * potencia(factorial (num), 2) * (2 * num + 1)
        resultado += (numero / den) * potencia (x, 2 * num + 1)
    return resultado

''' Fin de la funcion arcsen '''

''' creacion de la funcion para calcular la arccos de x '''
def arccos (x, termino=20):
    # Calcula arccos(x) a partir de  π/2 - arcsen(x)
    if x < -1 or x > 1: 
        return "Error: El valor de x debe estar entre -1 y 1"
    return (3.1415 / 2) - arcsen (x, termino)

'''Fin para la funcion arccos de x'''

'''Creacion de la funcion para calcular el seno hiperbolico de x'''
def senohiperbolico (x, termino=20):
    # Operacion para calcular senh(x) basados en su serie
    resultado = 0 
    for numero in range (termino):
        resultado += potencia (x, 2 * numero + 1) / factorial (2 * numero + 1)
    return resultado

''' Fin de la funcion seno hiperbolico '''

''' Creacion de la funcion coseno hiperbolico '''
def cosenohiperbolico(x, termino = 20):
    # Operacion para calcular cosh(x) basados en su serie
    resultado = 0 
    for numero in range (termino):
        resultado += potencia (x, 2 * numero) / factorial (2 * numero)
    return resultado

'''Fin de la funcion coseno hiperbolico '''

#Final de la creacion de operaciones matematicas basadas en series de taylor