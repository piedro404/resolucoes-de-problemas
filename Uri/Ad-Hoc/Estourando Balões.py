n = int(input())
baloes = list(map(int, input().split()))

flechasAtual = [0 for x in range(n+1)]
qtdFlechas = 0

for x in baloes:
    if flechasAtual[x] == 0:
        qtdFlechas+=1
        flechasAtual[x-1] += 1
    else:
        flechasAtual[x] -= 1
        flechasAtual[x-1] += 1

print(qtdFlechas)