def qtd_placas(dados):
    if dados[0] == 0 == dados[1]:
        return 0
    placas = (26**dados[0])*(10**dados[1])
    return placas

for _ in range(int(input())):
    print(qtd_placas(list(map(int, input().split()))))