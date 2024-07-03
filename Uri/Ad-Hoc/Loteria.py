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

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def result(points):
    if pontos == 3:
        return "terno"
    elif pontos == 4:
        return "quadra"
    elif pontos == 5:
        return "quina"
    elif pontos == 6:
        return "sena"
    
    return "azar"

pontos = 0
mega = list(map(int, input().split()))
numeros = quicksort(list(map(int, input().split())))

for num in mega:
    if binary_search(numeros, num) != -1:
        pontos += 1

print(result(pontos))
