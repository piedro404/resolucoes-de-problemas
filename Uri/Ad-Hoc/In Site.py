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

x = int(input())
lista = list(map(int, input().split()))
lista = quicksort(lista)
if(x%2!=0):
    print(lista[x//2])
else:
    print((lista[(x//2)-1]+lista[(x//2)])//2)
