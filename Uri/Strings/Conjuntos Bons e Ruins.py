def conjuntos(palavras):
    for x in range(len(palavras)-1):
        for y in range(x+1, len(palavras)):
            if (palavras[x] == palavras[y][0:len(palavras[x])]) or (palavras[y] == palavras[x][0:len(palavras[y])]):
                return "Conjunto Ruim"
        
    return "Conjunto Bom"
    
while True:
    x = int(input())
    if x == 0:
        break

    palavras = []
    for _ in range(x):
        palavras.append(str(input()))
    
    print(conjuntos(palavras))

        