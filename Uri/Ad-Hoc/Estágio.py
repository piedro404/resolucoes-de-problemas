i = 0
while True:
        x = int(input())
        if x == 0:
             break
        i+=1
        theBest = ""
        mPoint = 0
        for _ in range(x):
            dados = list(map(int, input().split()))
            if dados[1] > mPoint:
                mPoint = dados[1]
                theBest = ""
                theBest += str(dados[0]) + " "
            elif dados[1] == mPoint:
                theBest += str(dados[0]) + " "

        print(f"Turma {i}")
        print(theBest)
        print()
