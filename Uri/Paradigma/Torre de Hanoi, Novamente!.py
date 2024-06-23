import math

def findVara(varas, bola):
    for i, vara in enumerate(varas):
        if len(vara) == 0 or math.sqrt(vara[-1]+bola)%1==0:
            return i
    
    return -1

def hanoi(n):
    bola = 1
    varas = [[] for x in range(n)]
    while True:
        idx = findVara(varas, bola)
        if idx == -1:
            break
        
        varas[idx].append(bola)
        bola +=1
        
    return bola-1

for _ in range(int(input())):
    print(hanoi(int(input())))