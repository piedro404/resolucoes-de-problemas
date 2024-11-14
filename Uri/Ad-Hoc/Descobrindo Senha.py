def quicksort(matrix):
    if len(matrix) <= 1:
        return matrix
    pivot = matrix[len(matrix) // 2][1]
    left = []
    middle = []
    right = []
    for x in matrix:
        if x[1] > pivot:
            right.append(x)
        elif x[1] < pivot:
            left.append(x)
        else:
            middle.append(x)
            
    return quicksort(right) + middle + quicksort(left)


case = 1

while True:
    try:
        n = int(input())
        level_gordura = []

        for i, x in enumerate(list(map(float, input().split()))):
            level_gordura.append([i, x])

        level_gordura = quicksort(level_gordura)

        senha = ""
        for x in range(n):
            senha += str(level_gordura[x][0])

        print(f"Caso {case}: {senha}")
        case+=1
    except EOFError:
        break