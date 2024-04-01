def media_mediana(dados):
    return dados[0]*2 - dados[1]

while True:
    try:
        dados = list(map(int, input().split()))
        if dados[0] == 0 == dados[1]:
            break
        
        print(media_mediana(dados))
    except EOFError:
        break