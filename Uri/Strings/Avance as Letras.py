def calcDistanciaLetras(dados):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    distancia = 0

    for x in range(len(dados[0])):
        numD = alfabeto.index(dados[1][x])-alfabeto.index(dados[0][x])
        if numD < 0:
            numD += 26 

        distancia += numD

    return distancia

for _ in range(int(input())):
    print(calcDistanciaLetras(list(map(str, input().split()))))