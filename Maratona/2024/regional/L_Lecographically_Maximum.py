N = int(input())
BITS = 32
cnt = [0]*BITS

for k in list(map(int, input().split())):
    j = 0
    while(1<<j) <= k:
        if(1<<j) & k:
            cnt[j] += 1
        j += 1

for _ in range(N):
    prox = 0
    for j in range(BITS):
        if cnt[j] > 0:
            prox |= (1<<j)
            cnt[j] -= 1
    if _ < N-1:
        print(prox, end=" ")
    else:
        print(prox)
