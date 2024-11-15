while True:
    dados = list(map(int, input().split()))

    if dados[0] == 0 == dados[1]:
        break

    regra = [1, 1, 1, 1]
    matrix = []

    for _ in range(dados[0]):
        linha = list(map(int, input().split()))
        matrix.append(linha)

        questoesFeitas = sum(linha)
        
        if questoesFeitas == dados[1]:
            regra[0] = 0
        
        if questoesFeitas == 0:
            regra[3] = 0

    for x in range(dados[1]):
        resolvidas = 0
        for y in range(dados[0]):
            if matrix[y][x] == 1:
                resolvidas += 1
        
        if resolvidas == 0:
            regra[1] = 0
        
        if resolvidas == dados[0]:
            regra[2] = 0

    print(sum(regra))
