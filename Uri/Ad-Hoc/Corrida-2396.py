def quicksort(matr):
    if len(matr) <= 1:
        return matr
    pivot = matr[len(matr) // 2]
    left = []
    middle = []
    right = []
    for x in matr:
        if x[1] > pivot[1]:
            right.append(x)
        elif x[1] < pivot[1]:
            left.append(x)
        else:
            middle.append(x)
            
    return quicksort(left) + middle + quicksort(right)

placar = []

dados = list(map(int, input().split()))

for x in range(dados[0]):
    placar.append([x+1, sum(list(map(int, input().split())))])

placar = quicksort(placar)

for x in range(3):
    print(placar[x][0])
