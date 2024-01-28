def xp(b, xp):
    return b * xp

while True:
    dados = list(map(int, input().split()))
    if dados[0] == 0 and dados[1] == 0:
        break

    print(xp(dados[0], dados[1]))