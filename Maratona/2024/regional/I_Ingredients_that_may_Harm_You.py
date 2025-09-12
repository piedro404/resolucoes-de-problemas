ret = []
primos = []
def number_of_divisors(pos, mult):
    global ret, primos
    if pos == len(primos):
        ret.append(mult)
        return
    
    number_of_divisors(pos + 1, mult)
    number_of_divisors(pos + 1, mult * (-primos[pos]))

def fact(x):
    global fator, primos, ret
    primos.clear()
    while x > 1:
        p = fator[x]
        primos.append(p)
        while x % p == 0:
            x //= p

    ret.clear()
    number_of_divisors(0, 1)
    
MAXN = 100100
MAXV = 1000100
MOD = 1000000007

pr = [True] * MAXV
fator = [0] * MAXV

cnt = [0] * MAXV
pot2 = [1] * MAXN

pr[0] = pr[1] = False
pot2[1] = 2

for i in range(2, MAXN):
    pot2[i] = (pot2[i-1] * 2) % MOD

for i in range(2, MAXV):
    if pr[i]:
        fator[i] = i
        for j in range(i * i, MAXV, i):
            pr[j] = False
            fator[j] = i

n = int(input())
for x in map(int, input().split()):
    fact(x)
    for x in ret:
        cnt[abs(x)] += 1

q = int(input())
for x in range(q):
    fact(int(input()))
    sumC = 0
    for x in ret:
        sumC += cnt[abs(x)] * (-1 if x < 0 else 1)

    print(pot2[sumC])

# Otimizada 
    
MAXN = 100100
MAXV = 1000100
MOD = 1000000007

pot2 = [1] * MAXN
for i in range(1, MAXN):
    pot2[i] = (pot2[i-1] * 2) % MOD

mu = [1] * MAXV
is_prime = [True] * MAXV
is_prime[0] = is_prime[1] = False

for i in range(2, MAXV):
    if is_prime[i]:
        for j in range(i * i, MAXV, i):
            is_prime[j] = False
        
        for j in range(i, MAXV, i):
            mu[j] *= -1
        
        for j in range(i * i, MAXV, i * i):
            mu[j] = 0

n = int(input())
foods = list(map(int, input().split()))

freq = [0] * MAXV
for food in foods:
    freq[food] += 1

unique_foods = set(foods)
max_food = max(foods) if foods else 1

resp = [0] * MAXV

for d in range(1, max_food + 1):
    if mu[d] == 0:  
        continue
    
    count = 0
    for multiple in range(d, max_food + 1, d):
        count += freq[multiple]
    
    if count > 0:
        for multiple in range(d, MAXV, d):
            resp[multiple] += mu[d] * count

q = int(input())
for _ in range(q):
    allergy = int(input())
    print(pot2[resp[allergy]])