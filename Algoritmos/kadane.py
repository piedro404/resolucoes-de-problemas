def kadane_algorithm(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Exemplo de uso
array = [1, -3, 2, 1, -1]
result = kadane_algorithm(array)
print("Maior soma contígua:", result)
