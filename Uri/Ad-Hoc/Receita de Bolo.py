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

val = [
    2,
    3,
    5
]
dados = []

for e, x in enumerate(list(map(int, input().split()))):
    dados.append(x//val[e])

print(quicksort(dados)[0])

