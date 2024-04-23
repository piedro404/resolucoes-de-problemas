def conecta(linha1, linha2):
    for x in range(len(linha1)):
        if linha1[x] == linha2[x]:
            return "N"
        
    return "Y"

linha1 = list(map(int, input().split()))
linha2 = list(map(int, input().split()))

print(conecta(linha1, linha2))
