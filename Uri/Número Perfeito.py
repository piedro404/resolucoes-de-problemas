def listaDivisores(n) :
    divisores = 0
    for x in range(1, (n//2)+1):
        if n % x == 0:
            divisores += x

    if divisores == n:
        return f"{n} eh perfeito"

    return f"{n} nao eh perfeito"

v = int(input())

for _ in range(v):
    n = int(input())
    print(listaDivisores(n))