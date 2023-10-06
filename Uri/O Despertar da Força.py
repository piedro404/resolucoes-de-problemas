def radar(c, l, terreno):
    for x in range(c-1, c+2):
        for y in range(l-1, l+2):
            if x==c and y==l:
                continue

            if terreno[x][y] != 7:
                return False
            
    return True

def encontrarSabre(c, l, terreno):
    for j in range(1,c-1):
        for k in range(1, l-1):
            if terreno[j][k] == 42 and radar(j, k, terreno):
                return j+1, k+1
                
    return 0, 0

terreno = []
dados = list(map(int, input().split()))
for _ in range(dados[0]):
    terreno.append(list(map(int, input().split())))
    

pontos = (encontrarSabre(dados[0], dados[1], terreno))
print(pontos[0], pontos[1])