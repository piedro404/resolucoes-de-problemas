sumP = 0
qtdP = 0

for x in range(6):
    n = float(input())
    if n > 0:
        sumP += n
        qtdP += 1
        
print(f"{qtdP} valores positivos")
print("{:.1f}".format(sumP/qtdP))