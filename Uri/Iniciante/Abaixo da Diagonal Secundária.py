def calcMatriz(list, func):
    s = 0
    md = 0
    x=0
    for i in range(12): 
        for j in range(12-x, 12):
            s += list[i][j]
            md += 1
        x += 1

    if(func == "M"):
        s /= md

    return float(s)

func = input()
list = []
for x in range(12):
    listT = []
    for x in range(12):
        listT.append(float(input()))
    
    list.append(listT)

print("{:.1f}".format(calcMatriz(list, func)))