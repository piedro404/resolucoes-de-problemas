def ldsSum(lista, n):
    comb = []

    for i in range(1, n+1):
        for j in range(0, n-i+1):
            comb.append(lista[j:j+i])

    print(*comb)
    

n = 4
# lista = [6, 1, 5, 2, 4, 3]
lista = [4, 3, 1, 2]

print(ldsSum(lista, n))