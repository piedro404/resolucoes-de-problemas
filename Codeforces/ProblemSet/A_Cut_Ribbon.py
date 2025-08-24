def knapSack(capacity, val, wt):
    NEG = -10**9
    dp = [NEG] * (capacity + 1)
    dp[0] = 0  

    for i in range(len(val)):
        for j in range(wt[i], capacity + 1): 
            if dp[j - wt[i]] != NEG:
                dp[j] = max(dp[j], val[i] + dp[j - wt[i]])

    return dp[capacity]

n, a, b, c = map(int, input().split())
val = [1, 1, 1]
wt = [a, b, c]
capacity = n
print(knapSack(capacity, val, wt))