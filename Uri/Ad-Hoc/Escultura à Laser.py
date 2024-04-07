def lazer(a, alturas):
    vezes_ligado = a - alturas[0]
    prev = alturas[0]
    for x in range(1, len(alturas)):
        if prev > alturas[x]:
            vezes_ligado += prev - alturas[x]
        
        prev = alturas[x]

    return vezes_ligado

while True:
    a, c = map(int, input().split())
    # a, c = 5, 8
    if a == 0 and c == 0:
        break
    
    alturas = list(map(int, input().split()))
    # alturas = [1, 2, 3, 2, 0, 3, 4, 5]
        
    print(lazer(a, alturas))
    # break
