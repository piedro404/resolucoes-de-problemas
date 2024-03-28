def jogo(dados):
    if dados[0] == dados[2]:
        return int(dados[0])*int(dados[2])
    
    if dados[1] == dados[1].lower():
        return int(dados[0])+int(dados[2])
    
    return int(dados[2])-int(dados[0])

for _ in range(int(input())):
    print(jogo(str(input())))
