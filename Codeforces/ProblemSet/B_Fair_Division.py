# Simples
# for _ in range(int(input())):
#     dic = {
#         1: 0,
#         2: 0,
#     }
#     n = int(input())
#     for i in map(int, input().split()):
#         dic[i] = dic.get(i, 0) + 1
    
#     if ((dic[1]+(dic[2]*2)) % 2 == 0) and ((dic[1] > 0 and dic[1] % 2 == 0) or (dic[2] > 0 and dic[2] % 2 == 0)):
#         print("YES")
#     else:
#         print("NO")

# Complex
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


for _ in range(int(input())):
    n = int(input())
    values = list(map(int, input().split()))
    weights = values.copy()
    total_weight = sum(weights)

    if total_weight % 2 != 0:
        print("NO")
        continue

    capacity = total_weight // 2
    max_value = knapsack_01(values, weights, capacity)
    if max_value == capacity:
        print("YES")
    else:
        print("NO")