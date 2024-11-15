dados = list(map(int, input().split()))
linhasSum = [0 for x in range(dados[0])]
colunaSum = [0 for x in range(dados[1])]
maior = 0

for l in range(dados[0]):
    for i, c in enumerate(list(map(int, input().split()))):
        linhasSum[l] += c
        colunaSum[i] += c
        if maior < linhasSum[l]:
            maior = linhasSum[l]
        if maior < colunaSum[i]:
            maior = colunaSum[i]

print(maior)
