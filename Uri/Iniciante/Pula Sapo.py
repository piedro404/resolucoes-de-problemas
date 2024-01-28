def pulaSapo(p, canos):
    cAtual = canos[0]
    for x in range(1,len(canos)):
        if abs(cAtual - canos[x]) > p:
            return "GAME OVER"
        
        cAtual = canos[x]

    return "YOU WIN"

sapo = list(map(int, input().split()))
canos = list(map(int, input().split()))
print(pulaSapo(sapo[0], canos))