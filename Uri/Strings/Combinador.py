def cobinador(dados):
    newPalavra = []
    i = 0
    while True:
        c = 0
        if len(dados[0]) > i:
            newPalavra.append(dados[0][i])
        else:
            c +=1
        if len(dados[1]) > i:
            newPalavra.append(dados[1][i])
        else:
            c +=1
            
        if c == 2:
            break
        i+=1
        
    return "".join(newPalavra)

for _ in range(int(input())):
    print(cobinador(list(map(str, input().split()))))