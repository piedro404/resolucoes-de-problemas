for _ in range(int(input())):
    n, k = map(int, input().split())
    ca = []
    for i in range(n):
        ca.append(list(map(int, input().split())))

    ca.sort(key=lambda x: x[2])

    for x in ca:
        if k >= x[0] and k <= x[1]:
            k = max(k, x[2])

    print(k)