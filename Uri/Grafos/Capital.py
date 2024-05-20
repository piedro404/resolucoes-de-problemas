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
            
    return quicksort(left) + middle + quicksort(right)

def bloggs(dados):
    dados = quicksort(dados)
    
    if dados[0]*dados[3] == dados[1]*dados[2]:
        return "S"
    
    return "N"

print(bloggs(list(map(int, input().split()))))