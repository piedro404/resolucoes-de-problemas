def subset_sum(vector, mid, n):
    dp = [[False for x in range(mid+1)] for x in range(n+1)]

    dp[0][0] = True
    for x in range(1, n+1):
        for y in range(mid+1):
            dp[x][y] = dp[x-1][y]
            if(vector[x] <= y and dp[x-1][y-vector[x]]):
                dp[x][y] = True

    return dp[-1][-1]

print(subset_sum([0, 1, 2, 2, 3], 4, 4))