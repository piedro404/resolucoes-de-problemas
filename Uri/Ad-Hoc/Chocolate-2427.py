def min2(v):
    n = 1
    while 2**(n+1) <= v:
        n+=1

    return 2**n

n = min2(int(input()))

print(n*n)