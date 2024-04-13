def quebrou(dados):
    copos = 0
    for dado in dados:
        if dado[0] > dado[1]:
            copos += dado[1]
    
    return copos

dados = []
for _ in range(int(input())):
    dados.append(list(map(int, input().split())))
    
print(quebrou(dados))