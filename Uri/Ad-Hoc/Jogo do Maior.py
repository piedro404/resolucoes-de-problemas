def placar(dados):
    placar = [0, 0]
    for dado in dados:
        if dado[0] > dado[1]:
            placar[0] += 1
        elif dado[0] < dado[1]:
            placar[1] += 1
    
    return f"{placar[0]} {placar[1]}"

while True:
    dados = []
    n = int(input())
    if n == 0:
        break
    for x in range(n):
        dados.append(list(map(int, input().split())))
    print(placar(dados))