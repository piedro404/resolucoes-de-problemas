import math

l, a, p, r = map(int, input().split())

r = r*2

diagonalCaixa = math.sqrt(((l**2)+(a**2)+(p**2)))

if r>=diagonalCaixa:
    print("S")
else:
    print("N")