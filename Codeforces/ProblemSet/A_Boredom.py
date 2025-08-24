# Memoization approach (Top-down)
# def boredom(dic, seq, i, memo):
#     if i >= len(seq):
#         return 0
    
#     if i in memo:
#         return memo[i]

#     take = dic[seq[i]]
#     if i + 1 < len(seq) and seq[i+1] == seq[i] + 1:
#         take += boredom(dic, seq, i + 2, memo)  
#     else:
#         take += boredom(dic, seq, i + 1, memo)

#     not_take = boredom(dic, seq, i + 1, memo)
    
#     memo[i] = max(take, not_take)
#     return memo[i]

# dic = {}
# n = int(input())
# for i in map(int, input().split()):
#     dic[i] = dic.get(i, 0) + i

# # print(dic)
# print(boredom(dic, sorted(dic.keys()), 0, {}))

# Optimized DP approach
n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)
points = [0] * (max_val + 1)

for x in arr:
    points[x] += x

dp = [0] * (max_val + 1)
dp[1] = points[1]

for i in range(2, max_val + 1):
    dp[i] = max(dp[i-1], dp[i-2] + points[i])

print(dp[max_val])
