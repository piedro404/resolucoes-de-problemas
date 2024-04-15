dados = list(map(int, input().split()))
menorSaldo = dados[1]
for _ in range(dados[0]):
    dados[1] += int(input())
    if dados[1] < menorSaldo:
        menorSaldo = dados[1]

print(menorSaldo)