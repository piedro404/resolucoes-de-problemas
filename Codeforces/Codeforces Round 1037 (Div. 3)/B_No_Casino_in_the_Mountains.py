for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    p = 0
    h = 0

    for i in range(n):
        if p < k and a[i] == 0:
            p+=1
        else:
            if p == k:
                h +=1
            p = 0
    
    if p == k:
        h += 1

    print(h)