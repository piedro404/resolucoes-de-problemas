def kadane_algorithm(arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    if max_sum < 0:
        return 0
    
    return max_sum
    
while True:
    try:
        x = int(input())
        valores = []
        taxaPorDia = int(input())
        for _ in range(x):
            valores.append(int(input())-taxaPorDia)
        # print("Valor: " + str(kadane_algorithm(valores)))
        print(kadane_algorithm(valores))
    except EOFError:
        break
    