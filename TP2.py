# TP 2
import random

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
    capicua = False
    izquierda = lista[0]
    derecha = lista[len(lista)-1]
    for i in range(len(lista)):
        if izquierda == derecha:
            izquierda = izquierda + 1
            derecha = derecha - 1
            capicua = True
        else:
            return capicua
    return capicua

# main
# listaNueva = generar_lista_numeros()
# print(listaNueva)
listaPrueba = [50, 17, 91, 17, 50]

if esCapicua(listaPrueba):
    print("La lista es capicua")
else:
    print("La lista no es capicua")
"""
aEliminar = int(input("Digite el numero que quiere eliminar de la lista: "))
listaSinxElemento = elimina_valor(aEliminar, listaNueva)
print(listaSinxElemento)
"""