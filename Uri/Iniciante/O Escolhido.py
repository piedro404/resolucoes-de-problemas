def oEscolhido(alunos):
    nMaior=alunos[0][1]
    matAluno=alunos[0][0]

    for x in range(1,len(alunos)):
        if nMaior < alunos[x][1]:
            nMaior = alunos[x][1]
            matAluno = alunos[x][0]
    
    if nMaior >= 8:
        return int(matAluno)
    
    return "Minimum note not reached"


listaAlunos = []
for _ in range(int(input())):
    listaAlunos.append(list(map(float, input().split())))

print(oEscolhido(listaAlunos))
