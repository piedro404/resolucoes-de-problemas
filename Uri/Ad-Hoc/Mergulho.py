def herois(info, dados):
    if info[0] == info[1]:
        print("*")
        return

    hero = []
    for x in range(1, info[0]+1):
        if x not in dados:
            hero.append(str(x))    
        
    for x in hero:
        print(x, end=" ")
    print()
    

while True:
    try:
        info = list(map(int, input().split()))
        dados = list(map(int, input().split()))
        herois(info, dados)
    except EOFError:
        break