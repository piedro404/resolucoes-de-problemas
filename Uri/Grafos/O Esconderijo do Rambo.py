def estasSalvo(dados, grafos):
    for ponte in grafos:
        if len(ponte) % 2 != 0:
            return "Rambo esta perdido"
    
    return "Rambo esta salvo"

dados = list(map(int, input().split()))
grafos = [[] for _ in range(dados[0])]
for x in range(dados[1]):
    x, y = map(int, input().split())
    grafos[x].append(y)
    grafos[y].append(x)
    
print(estasSalvo(dados, grafos))