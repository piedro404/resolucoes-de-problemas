MAXN = 1001000

n, m = map(int, input().split())
vector = [[] for _ in range(MAXN)]
marc = [False]*MAXN
pai = [-1]*MAXN

marc[0] = True

def dfs(x: int):
    global marc, pai, vector
    marc[x] = True
    for i in vector[x]:
        if not(marc[i]):
            pai[i] = x
            dfs(i)

def id(x: int, m: int): 
    return x - m if x > m else x

for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in line[1:]:
        vector[i+m].append(j)
        vector[j].append(i+m)

for i in range(1, n+m+1):
    if not(marc[i]):
        pai[i] = -1
        dfs(i)

va, vb = [], []
for q in range(int(input())):
    a, b = map(int, input().split())

    va.clear()
    while a != -1:
        va.append(a)
        a = pai[a]

    vb.clear()
    while b != -1:
        vb.append(b)
        b = pai[b]

    if va[-1] != vb[-1]:
        print(-1)
    else:
        while len(va) > 1 and len(vb) > 1 and va[-2] == vb[-2]:
            va.pop()
            vb.pop()
        print((len(va)+len(vb)) // 2)
        result = []
        for i in va:
            result.append(id(i, m))
        for i in range(len(vb)-2, -1, -1):
            result.append(id(vb[i], m))
        print(*result)