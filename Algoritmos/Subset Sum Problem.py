def is_subset_sum(set, sum):
    n = len(set)
    dp = [[False] * (sum + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-set[i-1]]

    return dp[n][sum]

set = [3, 34, 4, 12, 5, 2]
sum = 9
print(is_subset_sum(set, sum))  # Output: True
