def troco(v, t):
    listaNotas = [2, 5, 10, 20, 50, 100]
    tc = t-v
    n = 0

    for x in reversed(listaNotas):
        if tc >= x:
            tc -= x
            n+=1

    if n == 2 and tc == 0:
        return "possible"

    return "impossible"

while True:
    dados = list(map(int, input().split()))
    if sum(dados)==0:
        break

    print(troco(dados[0], dados[1]))