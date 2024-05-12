def quicksort_reversed(arr):
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
            
    return quicksort_reversed(right) + middle + quicksort_reversed(left)

def viajante(dados):
    dados = quicksort_reversed(dados)
    if abs(dados[0]-dados[1]-dados[2]) == 0:
        return "S"
    
    if abs(dados[0]-dados[1]) == 0 or abs(dados[0]-dados[2]) == 0 or abs(dados[1]-dados[2]) == 0:
        return "S"
    
    return "N"

print(viajante(list(map(int, input().split()))))