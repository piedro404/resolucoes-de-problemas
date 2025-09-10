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

n = 90
print(fact(n))

# Optimized version using sieve

MAXN = 100100
MAXV = 1000100

pr = [True] * MAXV
fator = [0] * MAXV
cnt = [0] * MAXV

pr[0] = pr[1] = False

for i in range(2, MAXV):
    if pr[i]:
        fator[i] = i
        for j in range(i * i, MAXV, i):
            pr[j] = False
            fator[j] = i

def fact(x):
    global fator
    primos = []
    while x > 1:
        p = fator[x]
        primos.append(p)
        x //= p

    return primos

n = 90
print(fact(n))