# TP 2
import random
"""
# Ejercicio 1
# funciones
def generar_lista_numeros():
    cantidad_elementos = random.randint(10, 99) # Genera un número aleatorio de dos dígitos
    numeros = []
    for i in range(cantidad_elementos):
        numero = random.randint(1000, 9999) # Genera un número aleatorio de cuatro dígitos
        numeros.append(numero)
    return numeros

def suma_elementos(lista):
    suma = sum(lista)
    return suma

def elimina_valor(num, lista):
    for i in range(len(lista)):
        if i==num:
            lista.remove[i]
    return lista

def esCapicua(lista):
    longitud = len(lista)
    for i in range(longitud // 2):
        if lista[i] != lista[longitud - i - 1]:
            return False
    return True
"""

# Ejercicio 2
def listaCon50El():
    lista = []
    limite = 50
    for i in range(limite):
        numero = random.randint(0,100)
        lista.append(numero)
    return lista

def hayCopias(lista):
    copias = False
    lista.sort()
    for i in range(len(lista)):
        if lista[i] == lista[i+1]:
            return True
        else:
            ++i

def eliminarCopias(lista):
    nuevaLista = lista.copy()
    nuevaLista.sort()
    for i in nuevaLista:
        if i.count(nuevaLista[i]) > 1:
            nuevaLista.remove(nuevaLista[i])
    return nuevaLista
    




lista = [3,33,3,46,67,5,33,4,67,6,3,2,6,88,99]
listaSinRepetidos = eliminarCopias(lista)
print(listaSinRepetidos)
    