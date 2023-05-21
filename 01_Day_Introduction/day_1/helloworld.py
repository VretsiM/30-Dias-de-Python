#Ejercicios - Día 1
#Ejercicio: Nivel 1
#Compruebe la versión de Python que está utilizando
#Abra el shell interactivo de python y realice las siguientes operaciones. Los operandos son 3 y 4.
#suma (+)
print(3+4)
#sustracción(-)
print(4-3)
#multiplicación(*)
print(3*4)
#módulo(%)
print(4%3)
#división(/)
print(4/3)
#exponencial(**)
print(3**4)
#operador de división de piso(//)
print(4//3)
#Escriba cadenas en el shell interactivo de python. Las cadenas son las siguientes:
#Su nombre
print('mauro')
#tu apellido
print('villalba')
#Tu país
print('argentina')
#Estoy disfrutando de 30 días de python
print('Estoy disfrutando de 30 días de python')
#Compruebe los tipos de datos de los siguientes datos:
#10
print(type(10))
#9.8
print(type(9.8))
#3.14
print(type(3.14))
#4 - 4j
print(type(4-4j))
#['Asabeneh', 'Python', 'Finlandia']
print(type(['Asabeneh', 'Python', 'Finlandia']))
#Su nombre
print(type('mauro'))
#tu apellido
print(type('villalba'))
#Tu país
print(type('Argentina'))
#Ejercicio: Nivel 2
#Cree una carpeta llamada day_1 dentro de la carpeta 30DaysOfPython. Dentro de la carpeta day_1, cree un archivo python helloworld.py y repita las preguntas #1, 2, 3 y 4. Recuerde usar print() cuando esté trabajando en un archivo python. Navegue hasta el directorio donde ha guardado su archivo y ejecútelo.
#Ejercicio: Nivel 3
#Escriba un ejemplo para diferentes tipos de datos de Python, como número (entero, flotante, complejo), cadena, booleano, lista, tupla, conjunto y diccionario.
entero = 13
print(entero)
flotante = 13.5
print(flotante)
complejo = 4 + 2j
print(complejo)
cadena = "cadena"
print(cadena)
booleano = True
print(booleano)
lista = ['mauro','ricardo','villalba']
print(lista)
tupla = (1,2,3,4,5,'mauro')
print(tupla)
conjunto = {2,5,3,6}
print(conjunto)
diccionario = {
    'nombre':'mauro',
    'apellido' : 'villalba',
    'pais' : 'Argentina'
}
print(diccionario)
#Encuentra una distancia euclidiana entre (2, 3) y (10, 8)
from math import sqrt
distancia = sqrt((10-2)**2+(8-3)**2)
print(distancia)





