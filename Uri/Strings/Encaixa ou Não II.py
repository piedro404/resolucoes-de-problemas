def Encaixa(dados):
    if len(dados[1]) > len(dados[0]):
        return "nao encaixa"
    x = len(dados[0])-len(dados[1])
    pt = dados[0][x::]

    if dados[1] == pt:
        return "encaixa"
    
    return "nao encaixa"

for _ in range(int(input())):
    print(Encaixa(list(map(str, input().split()))))