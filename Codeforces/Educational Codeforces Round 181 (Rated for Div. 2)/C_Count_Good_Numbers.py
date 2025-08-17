from itertools import combinations

# + |A_2|                 # múltiplos de 2
# + |A_3|                 # múltiplos de 3
# + |A_5|                 # múltiplos de 5
# + |A_7|                 # múltiplos de 7
# - |A_2 ∩ A_3|           # múltiplos de 6
# - |A_2 ∩ A_5|           # múltiplos de 10
# - |A_2 ∩ A_7|           # múltiplos de 14
# - |A_3 ∩ A_5|           # múltiplos de 15
# - |A_3 ∩ A_7|           # múltiplos de 21
# - |A_5 ∩ A_7|           # múltiplos de 35
# + |A_2 ∩ A_3 ∩ A_5|     # múltiplos de 30
# + |A_2 ∩ A_3 ∩ A_7|     # múltiplos de 42
# + |A_2 ∩ A_5 ∩ A_7|     # múltiplos de 70
# + |A_3 ∩ A_5 ∩ A_7|     # múltiplos de 105
# - |A_2 ∩ A_3 ∩ A_5 ∩ A_7| # múltiplos de 210

def mult(lst):
    result = 1
    for x in lst:
        result *= x
    return result


primes = [2, 3, 5, 7]
freq = [4, 6, 4, 1]
comb = []

for k in range(1, len(primes) + 1):
    for subset in combinations(primes, k):
        comb.append(mult(subset))


def primosValue(n):
    multiplosT = 0
    s = True
    idx = 0

    for x in freq:
        multiplosP = 0
        for y in range(idx, idx + x):
            if s:
                multiplosP += n // comb[y]
            else:
                multiplosP -= n // comb[y]

        multiplosT += multiplosP

        s = not s
        idx += x

    return multiplosT


def primosBetweenValues(l, r):
    goods = r - l + 1
    bads = primosValue(r) - primosValue(l - 1)

    return goods - bads


for _ in range(int(input())):
    l, r = map(int, input().split())

    print(primosBetweenValues(l, r))
