dados = list(map(int, input().split()))
pontas = list(map(int, input().split()))

qtd = 0

for x in range(1, dados[0]):
    if pontas[x-1] < pontas[x] and pontas[x+1] < pontas[x]:
        qtd +=1

if qtd == dados[1]:
    print("beautiful")
else:
    print("ugly")