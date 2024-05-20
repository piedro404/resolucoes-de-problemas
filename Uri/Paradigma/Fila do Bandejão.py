def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for x in arr:
        if x > pivot:
            right.append(x)
        elif x < pivot:
            left.append(x)
        else:
            middle.append(x)
            
    return quicksort(right) + middle + quicksort(left)

def diferencia(dados):
    dif = []
    for x in range(len(dados)-1):
        dif.append(dados[x+1]-dados[x])

    return quicksort(dif)

def fila(n, dados):
    dados.insert(0, 0)
    dif = diferencia(dados)
    return sum(dif)  - sum(dif[:n-1])
    
while True:
    try:
        infos = list(map(int, input().split()))
        dados = list(map(int, input().split()))
        print(fila(infos[1], dados))
    except EOFError:
        break