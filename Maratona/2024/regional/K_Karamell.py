def subset_sum(vector, mid, n):
    dp = [[False for x in range(mid+1)] for x in range(n+1)]

    dp[0][0] = True
    for x in range(1, n+1):
        for y in range(mid+1):
            dp[x][y] = dp[x-1][y]
            if(vector[x] <= y and dp[x-1][y-vector[x]]):
                dp[x][y] = True

    return dp

def main():
    n = int(input())
    vector = [0]
    mid = 0

    for x in list(map(int, input().split())):
        vector.append(x)
        mid+=x

    if(mid%2==1):
        print("-1")
        return 

    mid //= 2
    dp = subset_sum(vector, mid, n)

    if(not(dp[-1][-1])):
        print("-1")
        return 

    sub1 = []
    sub2 = []
    ref = mid
    for x in range(n, 0, -1):
        if(ref >= vector[x] and dp[x-1][ref-vector[x]]):
            sub1.append(vector[x])
            ref -= vector[x]
        else:
            sub2.append(vector[x])            
    
    result = []
    s1, s2 = 0, 0
    for x in range(n):
        if(s1<=s2):
            result.append(sub1.pop())
            s1 += result[-1]
        else:
            result.append(sub2.pop())
            s2 += result[-1]
    
    print(*result)

main()