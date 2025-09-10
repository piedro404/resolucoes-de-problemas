def sieve_of_eratosthenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i*i, n+1, i):
                is_prime[multiple] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

print(sieve_of_eratosthenes(int(input())))

# Logicamente similar ao código abaixo, porem, salva os primos em uma lista para ser usada posteriormente.:

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

primes = []
for x in range(int(input())):
    if pr[x]:
        primes.append(x)

print(primes)
