def arvoreEscolhida(dados):
    if (dados[0] >= 200 and dados[0] <= 300) and (dados[1] >= 50) and (dados[2] >= 150):
        return "Sim"
    
    return "Nao"

for _ in range(int(input())):
    print(arvoreEscolhida(list(map(int, input().split()))))
