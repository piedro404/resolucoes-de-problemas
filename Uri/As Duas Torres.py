def palatir(dados):
    return dados[0] / sum(dados[1::])

dados = list(map(int, input().split()))
print("{:.2f}".format(palatir(dados)))