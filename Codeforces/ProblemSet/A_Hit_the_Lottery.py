qtd_cell = 0
cell = [100, 20, 10, 5, 1]

n = int(input())

for c in cell:
    qtd_cell += n // c
    n = n % c

print(qtd_cell)