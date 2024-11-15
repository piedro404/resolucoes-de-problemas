entrada = list(map(int, input().split()))

maiorS = 1
seq = 1
dados = list(map(int, input().split()))
for x in range(1, len(dados)):
    if dados[x-1]+entrada[1] >= dados[x]:
        seq +=1
        if maiorS < seq:
            maiorS = seq
    else:
        seq = 1

print(maiorS)