n = int(input())
sA = 1
s = 1
lista = list(map(int, input().split()))
 
for x in range(1, len(lista)):
    if lista[x-1] < lista[x]:
        s += 1
        sA = max(sA, s)
    else:
        s = 1
 
print(sA)