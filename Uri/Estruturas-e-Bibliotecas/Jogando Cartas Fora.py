def cartas(n):
    monte = list(range(1,n+1))
    discartadas = []
    
    while len(monte) != 1:
        discartadas.append(str(monte.pop(0)))
        monte.append(monte.pop(0))
    
    print(f"Discarded cards: {', '.join(discartadas)}")
    print(f"Remaining card: {monte[0]}")

while True:
    n = int(input())
    if n == 0:
        break
    
    cartas(n)

