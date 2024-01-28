def calcMatriz(list, func):
    s = 0
    md = 0
    for i in range(12): 
        for j in range(12-i, 12):
            if(j>i):
                s += list[i][j]
                md += 1

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