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

# Exemplo de uso
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)  # Saída: [1, 1, 2, 3, 6, 8, 10]
