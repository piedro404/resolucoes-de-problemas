def imparPar(n, o):
    if n % 2 == 0:
        if o == 1:
            return "Jogador 1 ganha!"
        return "Jogador 2 ganha!"
    else:
        if o == 0:
            return "Jogador 1 ganha!"
        return "Jogador 2 ganha!"

def imparParRoubo(dados):
    s = dados[1] + dados[2]
    if dados[3] == 0 and dados[4] == 0:
        resultado = imparPar(s, dados[0])
        return resultado
    elif dados[3] == dados[4]:
        return "Jogador 2 ganha!"
    elif dados[3] == 1:
        return "Jogador 1 ganha!"
    else:
        return "Jogador 1 ganha!"

dados = list(map(int, input().split()))
resultado = imparParRoubo(dados)
print(resultado)
