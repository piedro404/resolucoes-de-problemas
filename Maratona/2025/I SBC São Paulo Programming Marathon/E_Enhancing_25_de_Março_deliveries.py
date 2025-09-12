from operator import itemgetter

MAXN = 100100
best = [0] * MAXN

n, d = map(int, input().split())
v = [tuple(map(int, input().split())) for _ in range(n)]

v.sort(key=itemgetter(0))  

su = best[0] = v[0][1]
resp = 0
j = 0
for i in range(n):
    while j+1 < n and v[j+1][0] - v[i][0] <= d:
        su+=v[j+1][1]
        j+=1
        best[j] = max(best[j-1], su)
    
    resp = max(resp, su + (best[i-1] if i > 0 else 0))
    su -= v[i][1]

print(resp)
    
