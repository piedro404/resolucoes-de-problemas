def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

def knapSack(capacity, weights, values, n):
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    result = K[n][capacity]

    w = capacity
    items_chosen = []
    for i in range(n, 0, -1):
        if result <= 0:
            break
        if result == K[i - 1][w]:
            continue
        else:
            items_chosen.append(i - 1)
            result -= values[i - 1]
            w -= weights[i - 1]

    return K[n][capacity], items_chosen

# Exemplo de uso
# values = [60, 100, 120]
# weights = [10, 20, 30]
# capacity = 50

values = [10, 40, 15, 90]
weights = [1, 1, 2, 3]
capacity = 4
n = 4

max_value = knapsack_01(values, weights, capacity)
print("Valor máximo obtido:", max_value)

kap = knapSack(capacity, weights, values, n)
print(kap)