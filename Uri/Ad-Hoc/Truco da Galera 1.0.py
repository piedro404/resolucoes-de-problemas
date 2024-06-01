def truco(cartas):
    q, j, k, a = 0, 0, 0, 0
    
    for c in cartas:
        if q == 0 and c == "Q":
            q += 1
        elif j == 0 and c == "J":
            j += 1
        elif k == 0 and c == "K":
            k += 1
        elif a == 0 and c == "A":
            a += 1
            
    if q == j == k == a == 1:
        return "Aaah muleke"
    
    return "Ooo raca viu"

for _ in range(int(input())):
    print(truco(str(input())))