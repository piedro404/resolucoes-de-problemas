estrada = list(map(int, input().split()))
precos = list(map(int, input().split()))

preco_total = estrada[0]*precos[0]+((estrada[0]//estrada[1])*precos[1])
print(preco_total)