import math


def ladoTerreno(casaL1, casaL2, porc):
    areaCasa = casaL1*casaL2
    areaTerreno = (areaCasa*100)/porc
    ladoTerreno = math.sqrt(areaTerreno)
    
    return int(ladoTerreno)

while True:
    dados = list(map(int, input().split()))
    if dados[0] == 0:
        break
    
    print(ladoTerreno(dados[0], dados[1], dados[2]))