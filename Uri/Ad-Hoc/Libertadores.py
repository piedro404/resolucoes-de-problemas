
for _ in range(int(input())):
    gols = [0, 0]
    golsCasa = [0, 0]
    pontos = [0, 0]
    for i in range(2):
        inputs = input().split()
        time1 = 0
        time2 = 0

        if i == 0:
            time1 = int(inputs[0])   
            time2 = int(inputs[2])
            golsCasa[0] += time2
        else:
            time1 = int(inputs[2])   
            time2 = int(inputs[0])  
            golsCasa[1] += time1

        gols[0] += int(time1)
        gols[1] += int(time2)

        if time1 > time2:
            pontos[0] += 3
        elif time2 > time1:
            pontos[1] += 3
        else:
            pontos[0] += 1
            pontos[1] += 1
    
    if pontos[0] > pontos[1]:
        print("Time 1")
    elif pontos[1] > pontos[0]:
        print("Time 2")
    else:
        if gols[0] > gols[1]:
            print("Time 1")
        elif gols[1] > gols[0]:
            print("Time 2")
        else:
            if golsCasa[0] < golsCasa[1]:
                print("Time 1")
            elif golsCasa[1] < golsCasa[0]:
                print("Time 2")
            else:
                print("Penaltis")
        