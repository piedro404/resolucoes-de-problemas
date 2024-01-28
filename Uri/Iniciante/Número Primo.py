import math

def eh_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limite = math.isqrt(n) + 1
    for x in range(3, limite, 2):
        if n % x == 0:
            return False
        
    return True

v = int(input())

for _ in range(v):
    n = int(input())
    if eh_primo(n):
        print(f"{n} eh primo")
    else:
        print(f"{n} nao eh primo")