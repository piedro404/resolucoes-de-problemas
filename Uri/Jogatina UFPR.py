def playerRaiz(cs, facul):
    return cs.count(facul)

while True:
    try:
        cs = []
        dados = list(map(int, input().split()))
        for _ in range(dados[0]):
            gmpy = list(map(int, input().split()))
            if gmpy[1] == 0:
                cs.append(gmpy[0])

        print(playerRaiz(cs, dados[1]))
    except EOFError:
        break
