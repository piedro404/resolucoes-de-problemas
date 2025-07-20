def verifyDeranged(b, c):
    nMatchs = []
    for x in range(len(b)):
        if b[x] != c[x]:
            nMatchs.append(b[x])

    return nMatchs

for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    c = sorted(b)

    nMatchs = verifyDeranged(b, c)

    if len(nMatchs):
        print("YES")
        print(len(nMatchs))
        print(*nMatchs)
    else:
        print("NO")
    