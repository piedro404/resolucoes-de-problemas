lista = {
    "A":0,
    "E":0,
    "H":0,
    "M":0,
    "X":0
}

for _ in range(int(input())):
    dados = list(map(str,input().split()))
    lista[dados[1]] += 1

print(f"{lista['X']} Hobbit(s)")
print(f"{lista['H']} Humano(s)")
print(f"{lista['E']} Elfo(s)")
print(f"{lista['A']} Anao(oes)")
print(f"{lista['M']} Mago(s)")