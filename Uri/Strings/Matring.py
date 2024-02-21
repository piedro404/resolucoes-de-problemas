def decodificar_matring(matring):
    linhas = 4
    colunas = len(matring[0])
    # print(linhas, colunas)

    F, L = "", ""
    for x in range(4):
        F += str(matring[x][0])
        L += str(matring[x][colunas-1])

    # print(F, L)

    decod = ""

    for j in range(1, colunas-1):
        Mi = ""
        for x in range(4):
            Mi += str(matring[x][j])

        Ci = (int(F) * int(Mi) + int(L)) % 257
        decod += chr(Ci)

    return decod        

matring = []
for _ in range(4):
    matring.append(str(input()))

result = decodificar_matring(matring)
print(result)