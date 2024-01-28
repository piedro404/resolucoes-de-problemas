dados1 = list(map(int, input().split()))
dados2 = list(map(int, input().split()))

faltou = 0
for x in range(3):
    if dados2[x] > dados1[x]:
        faltou += dados2[x] - dados1[x]

print(faltou)