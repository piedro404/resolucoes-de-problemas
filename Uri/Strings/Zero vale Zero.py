def somaSemZero(dados):
    result = str(dados[0] + dados[1])
    return result.replace("0", "")

while True:
    dados = list(map(int, input().split()))
    if dados[0] == 0 and dados[1] == 0:
        break

    print(somaSemZero(dados))
