def knapsack_01(capacity, bombas, n):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if bombas[i - 1][1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - bombas[i - 1][1]] + bombas[i - 1][0])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

for _ in range(int(input())):
    bombas = []
    for _ in range(int(input())):
        bombas.append(list(map(int, input().split())))

    capacity = int(input())
    meta = int(input())

    if knapsack_01(capacity, bombas, len(bombas)) >= meta:
        print("Missao completada com sucesso")
    else:
        print("Falha na missao")
