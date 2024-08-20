def culpado(lista, idx):
    while True:
        if idx == lista[idx-1]:
            return lista[idx-1]
        idx = lista[idx-1]

while True:
    x = int(input())
    if x ==0:
         break
    dados = list(map(int, input().split()))
    start = int(input())
    print(culpado(dados, start))
