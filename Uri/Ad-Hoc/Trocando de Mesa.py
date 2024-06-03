def trade(mesas, a, b):
    temp = mesas[a] 
    mesas[a] = mesas[b]
    mesas[b] = temp

def query(mesas, a):
    red = 0
    current = a
    while mesas[current-1] != a:
        red +=1
        current = mesas[current-1]
    
    return red


mesas = [x+1 for x in range(int(input()))]
for _ in range(int(input())):
    dados = list(map(int, input().split()))
    if dados[0] == 1:
        trade(mesas, dados[1]-1, dados[2]-1)
    else:
        print(query(mesas, dados[1]))