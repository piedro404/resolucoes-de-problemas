def alertBomb(x, campo):
    if x != 0:
        campo[x-1] +=1

    if x != len(campo)-1:
        campo[x+1] +=1
    
    campo[x] +=1

    return campo

campo = [0] * int(input())

for x in range(len(campo)):
    hasBomb = int(input())
    if hasBomb:
        campo = alertBomb(x, campo)

for x in campo:
    print(x)