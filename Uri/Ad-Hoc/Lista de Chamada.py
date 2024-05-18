dados = list(map(int, input().split()))
lista = []
for _ in range(dados[0]):
    lista.append(str(input()))
lista.sort()
print(lista[dados[1]-1])