sets = [0, 0]
pontos = [0, 0]
saque = False
isEndGame = False
winner = -1
def main():
    global saque
    def endSet(id, rId):
        global pontos, sets, isEndGame, winner
        if (pontos[id] > pontos[rId] and pontos[id] > 4 and pontos[id]-pontos[rId] > 1) or (pontos[id] == 10):
            sets[id] += 1
            if sets[id] == 2:
                isEndGame = True
                winner = id
            pontos = [0, 0]
    
    def setPoints(saque):
        global pontos
        if not(saque):
            pontos[0] += 1
            endSet(0, 1)
        else:
            pontos[1] += 1
            endSet(1, 0)
    
    def printGame(saque):
        global pontos, sets, isEndGame, winner
        if isEndGame:
            if winner == 0:
                print(f"{sets[0]} (winner) - {sets[1]}")
            else:
                print(f"{sets[0]} - {sets[1]} (winner)")
        elif not(saque):
            print(f"{sets[0]} ({pontos[0]}*) - {sets[1]} ({pontos[1]})")
        else:
            print(f"{sets[0]} ({pontos[0]}) - {sets[1]} ({pontos[1]}*)")
    
    for a in input():
        if a == "S":
            setPoints(saque)
        elif a == "R":
            saque = not(saque)
            setPoints(saque)
        else:
            printGame(saque)

if __name__ == "__main__":
    main()
