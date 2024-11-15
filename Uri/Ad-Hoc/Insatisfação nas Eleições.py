def ganhador(cadidatos, votos):
    for x in range(len(cadidatos)):
        if cadidatos[x] / votos > 0.50:
            return x+1
    return -1

for _ in range(int(input())):
    dados = list(map(int, input().split()))
    cadidatos = [0 for x in range(dados[0])]

    for x in list(map(int, input().split())):
        cadidatos[x-1] +=1

    print(ganhador(cadidatos, dados[1]))