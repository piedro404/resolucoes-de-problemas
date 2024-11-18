import math

def quicksort(matrix):
    if len(matrix) <= 1:
        return matrix
    pivot = matrix[len(matrix) // 2][0]
    left = []
    middle = []
    right = []
    for x in matrix:
        if x[0] > pivot:
            right.append(x)
        elif x[0] < pivot:
            left.append(x)
        else:
            middle.append(x)
            
    return quicksort(left) + middle + quicksort(right)

dados = list(map(int, input().split()))
peoples = []
for x in range(dados[1]):
    peoples.append(list(map(int, input().split())))

peoples = quicksort(peoples)

graus = math.radians(dados[0])
distancia = 0


