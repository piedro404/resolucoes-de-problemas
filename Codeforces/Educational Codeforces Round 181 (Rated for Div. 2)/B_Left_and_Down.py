import math
 
t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    mdc = math.gcd(a, b)
    dx = a // mdc
    dy = b // mdc
 
    if dx <= k and dy <= k:
        print(1)
    else:
        print(2)