import numpy
from heapq import *

import pylab as pl

def heuristica(inicio, final):
    return (final[0] - inicio[0]) ** 2 + (final[1] - inicio[1]) ** 2

def aestrella(mapa, inicio, fin):

    vecinos = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

    listaCerrada = [] #Nodos
    anteriores = {} #Nodo anterior en el camino menos costoso
    gCalculo = {inicio:0} #Menor costo entre el nodo actual y el inicial
    fCalculo = {inicio:heuristica(inicio, fin)} #Costo total
    listaAbierta = [] #Lista abierta -> Nodos por verificar

    heappush(listaAbierta, (fCalculo[inicio], inicio)) #agrega el nodo al listaAbierta manteniendo la forma del listaAbierta
    
    while listaAbierta:

        actual = heappop(listaAbierta)[1] #el nodo en la lista abierta que tiene el valor de f más bajo

        if actual == fin:
            camino = []
            while actual in anteriores:
                camino.append(actual)
                actual = anteriores[actual]
            return camino
        listaCerrada.append(actual)
        # Para los vecinos, verifica las distancias entre el proximo nodo y el final para tomar la ruta de menos costo                
        for i, j in vecinos:
            vecino = actual[0] + i, actual[1] + j            
            tmpG = gCalculo[actual] + heuristica(actual, vecino) #distancia desde el inicio hasta el vecino pasando por el nodo actual
            if 0 <= vecino[0] < mapa.shape[0]: #verifica el camino por donde puede seguir en i
                if 0 <= vecino[1] < mapa.shape[1]: #Verifica el camino por donde puede seguir en j               
                    if mapa[vecino[0]][vecino[1]] == 1: #Verifica que pueda seguir por uno de sus vecinos
                        continue
                else:
                    # No es un camino
                    continue
            else:
                # No es un camino
                continue
            
            if vecino in listaCerrada and tmpG >= gCalculo.get(vecino, 0): #Si el camino por uno de sus vecinos tiene mayor costo, lo descarta
                continue
                
            if  tmpG < gCalculo.get(vecino, 0) or vecino not in [i[1]for i in listaAbierta]: #Encuentra el camino más optimo y lo recorre
                anteriores[vecino] = actual
                gCalculo[vecino] = tmpG
                fCalculo[vecino] = tmpG + heuristica(vecino, fin)
                heappush(listaAbierta, (fCalculo[vecino], vecino)) #Agrega al listaAbierta el costo total del nodo
                
    return False #No hay nodos por verificar, pero no se llego al final


mapa = numpy.array(
    [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,1,1],
    [1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,1,1,1],
    [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1],
    [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,1,0,1,1,1],
    [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,1,1],
    [1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,0,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1]])

copiaMap = mapa

pl.matshow(mapa)
    
print("Entradas:\n -1. CDL\n -2. Principal\n -3. Ceibas")
print("Destinos:")
print(" 4. Acacias\n 5.Palmas\n 6.Central \n 7.Lago\n 8.Campus Nova\n 9.Almendros\n 10.Guayacanes\n 11.Educon\n")
#while True:
inicio = int(input("Lugar de inicio: "))

if(inicio == 1): #CDL
    inicial = (23,4)
elif(inicio == 2): #Principal
    inicial = (29,25)
elif(inicio == 3): #ceibas
    inicial = (1,5)
        
    
finalLugar = int(input("Lugar final: "))

if (finalLugar == 4): #Acacias
    final = (3,18)
elif (finalLugar == 5): #Palmas
    final = (23,34)
elif (finalLugar == 6): #Central
    final = (22,32)
#elif (finalLugar == 7): #Biblioteca
#    final = (21,29)
elif (finalLugar == 7): #Lago
    final = (14,29)
elif (finalLugar == 8): #Campus Nova
    final = (13,1)
elif (finalLugar == 9): #Almendros
    final = (18,14)
#elif (finalLugar == 11): #Saman
#    final = (14,17)
elif (finalLugar == 10): #Guayacanes
    final = (18,32)
elif (finalLugar == 11): #Educon
    final = (19,20)

inicio = inicial
fin = final

path = aestrella(mapa, inicio,fin)

print(path)

for element in path:
    copiaMap[element[0]][element[1]]= 3

pl.matshow(copiaMap)



#http://code.activestate.com/recipes/578919-python-a-pathfinding-with-binary-heap/
#https://en.wikipedia.org/wiki/A*_search_algorithm