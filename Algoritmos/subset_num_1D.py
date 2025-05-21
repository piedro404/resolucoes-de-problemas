def subset_sum(arr, x):
    dp = [False] * (x + 1)
    dp[0] = True

    for v in arr:
        for s in range(x, v - 1, -1):
            if dp[s - v]:
                dp[s] = True

    return dp[x], dp

res, dp = subset_sum([1, 2, 3, 2], 4)   

print(dp)
