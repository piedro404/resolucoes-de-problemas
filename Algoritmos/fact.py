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

n = 143
print(fact(n))