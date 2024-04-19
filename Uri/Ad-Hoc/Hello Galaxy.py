def planetas(dados):
    planetaM = dados[0][0]
    anoM = int(dados[0][1]) - int(dados[0][2])
    for x in range(1, len(dados)):
        ano = int(dados[x][1]) - int(dados[x][2])
        if anoM > ano:
            anoM = ano
            planetaM = dados[x][0]
            
    return planetaM

while True:
    n = int(input())
    if n == 0:
        break
    dados = []
    for _ in range(n):
        dados.append(list(map(str, input().split())))
    print(planetas(dados))