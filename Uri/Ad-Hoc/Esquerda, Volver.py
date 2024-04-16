def dire(rotas):
    rosas_ventos = ["N", "L", "S", "O"]
    i = 0
    for x in rotas:
        if x == "D":
            if i == 3:
                i = 0
            else:
                i+=1
        else:
            if i == 0:
                i = 3
            else:
                i-=1
    
    return rosas_ventos[i]
    
while True:
    n = int(input())
    if n == 0:
        break
    print(dire(str(input())))
