def tiraVela(dados):
    porta = "A porta abriu!" if dados[2] == 1 else "A porta fechou!"
    return "{:02d}:{:02d} - {}".format(dados[0], dados[1], porta)


for _ in range(int(input())):
    dados = list(map(int, input().split()))
    print(tiraVela(dados))
    