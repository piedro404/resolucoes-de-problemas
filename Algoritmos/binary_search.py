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

# Exemplo de uso
sorted_arr = [1, 2, 3, 6, 8, 10]
target = 6
index = binary_search(sorted_arr, target)
print(index)  # Saída: 3 (índice do elemento 6 no array)
