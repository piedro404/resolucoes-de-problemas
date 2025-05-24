def fact(n):
    i = 2
    fact = []
    while i * i <= n:
        while n % i == 0:
            fact.append(i)
            n //= i 
        i += 1
    if n > 1:
        fact.append(n)

    return fact

y, k = map(int, input().split())

if y == 1:
    print(1*k+1)
else:
    fac = fact(y)
    i = fac[0]-1
    x = fac[0]
    # print(i, x)

    for p in range(1, len(fac)):
        if i+fac[p]-1 <= k:
            i+= fac[p]-1
            x*= fac[p]
            # print(i, x)
        else:
            break

    # print(k, i)
    if k > i:
        x += (k-i)*x

    print(x)