def descriptrografia(texto, chaves):
    textoDes = ""
    for c in chaves:
        textoDes += texto[c-1]

    return textoDes

while True:
    try:
        texto = str(input())
        int(input())
        dados = list(map(int, input().split()))
        print(descriptrografia(texto, dados))
    except EOFError:
        break