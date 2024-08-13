def quicksort(matrix, m):
    if len(matrix) <= 1:
        return matrix
    pivot = matrix[len(matrix) // 2][1]
    left = []
    middle = []
    right = []
    for x in matrix:
        if x[1] <= m:
            if x[1] > pivot:
                right.append(x) 
            elif x[1] < pivot:
                left.append(x)
            else:
                middle.append(x)
            
    return quicksort(right, m) + middle + quicksort(left, m)

def maiorEntraga(idx=0, carga=0):
    global entregas, m, memo
    if carga >= m or idx >= len(entregas):
        return 0
    
    if (idx, carga) in memo:
        return memo[(idx, carga)]

    if carga+entregas[idx][1] <= m:
        tempo1 = entregas[idx][0] + maiorEntraga(idx+1, carga+entregas[idx][1])
    else:
        tempo1 = maiorEntraga(idx+2, carga)
        
    tempo2 = maiorEntraga(idx+1, carga)
    
    memo[(idx, carga)] = max(tempo1, tempo2)
    return memo[(idx, carga)]

while True:    
    x = int(input())
    if x == 0:
        break
    entregas = []
    memo = {}
    m = int(input())    
    for _ in range(x):
        entregas.append(list(map(int, input().split())))
    entregas = quicksort(entregas, m)
    for x in range(len(entregas), -1, -1):
        maiorEntraga(x, 0)
    # print(entregas)
    # print(memo)
    print(str(maiorEntraga()) + " min.")
    