dados = list(map(int, input().split()))
for _ in range(dados[1]):
    resp = str(input())
    if resp == "fechou":
        dados[0]+=1
    else:
        dados[0]-=1

print(dados[0])
    