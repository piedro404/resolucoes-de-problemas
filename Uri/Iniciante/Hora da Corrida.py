import math

def corridaPorc(dados):
    perc = dados[0]*dados[1]
    porcPerc = []

    for x in range(10, 100, 10):
        porcPerc.append(math.ceil(perc*(x/100)))

    return porcPerc

dados = list(map(int, input().split()))
print(" ".join(map(str, corridaPorc(dados))))