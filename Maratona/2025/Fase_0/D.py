n = int(input())
etd1 = input()
etd2 = input()

qtdT = 0
td = 0

for x in range(n):
    if etd1[x] == "*":
        qtdT+=1
        if etd2[x] == "*":
            td+=1

print(f"{1-(td/qtdT):.2f}")
