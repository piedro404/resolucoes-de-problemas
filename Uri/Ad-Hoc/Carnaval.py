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

notas = quicksort(list(map(float, input().split())))
sum = 0
for x in range(1, len(notas)-1):
    sum += notas[x]

print("{:.1f}".format(sum))

