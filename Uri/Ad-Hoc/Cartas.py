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

dados = list(map(int, input().split()))
orderDados = quicksort(dados)

if dados == orderDados:
    print("C")
elif dados == orderDados[::-1]:
    print("D")
else:
    print("N")