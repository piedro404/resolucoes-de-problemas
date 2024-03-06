def exigencia_Carmem(dados):
    if dados[0] == "cachorro":
        if len(dados[2]) > 1:
            for p_nome in dados[2]:
                if p_nome[0] == dados[1][0]:
                    return 1
    
    return 0

while True:
    try:
        result = 0
        for _ in range(int(input())):
            dados = []
            dados.append(str(input()))
            dados.append(str(input()))
            dados.append(list(input().split()))

            result += exigencia_Carmem(dados)
            input()

        print(result)

    except EOFError:
        break
