def maquina(A, B, C):
    volume = A*B*C
    arresta = volume**(1/3)
    
    return int(arresta)

while True:
    A, B, C = map(int, input().split())
    if A == B == C == 0:
        break
    
    print(maquina(A, B, C))
    
    