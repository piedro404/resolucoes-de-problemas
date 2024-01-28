def forcaAtaque(bn, poke):
    b = 0
    if poke[2] % 2 == 0:
        b = bn
    
    return ((poke[0]+poke[1])/2)+b

def btlPoke(bn, poke1, poke2):
    pk1 = forcaAtaque(bn, poke1)
    pk2 = forcaAtaque(bn, poke2)
    if pk1 < pk2:
        return "Guarte"
    
    if pk1 > pk2:
        return "Dabriel"
    
    return "Empate"

for _ in range(int(input())):
    bn = int(input())
    poke1 = list(map(int, input().split()))
    poke2 = list(map(int, input().split()))
    print(btlPoke(bn, poke1, poke2))