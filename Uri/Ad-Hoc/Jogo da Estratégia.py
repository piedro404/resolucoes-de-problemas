dados = list(map(int, input().split()))
pontos = list(map(int, input().split()))

mIdx = 0
mPoint = 0
pontosPlayer = [0 for x in range(dados[0])]

for x in range(len(pontos)):
    idx = x%dados[0]
    pontosPlayer[idx] += pontos[x]
    if pontosPlayer[idx] >= mPoint:
        mPoint = pontosPlayer[idx]
        mIdx = idx

print(mIdx+1)