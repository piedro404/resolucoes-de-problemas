def isPossibleWithTwoConj(conj):
    v1, v2 = 1, 2
    aux = 0

    for x in conj[0]:
        aux = x
        if (aux < v1):
            return "N"
        
        v1 = aux

    for x in conj[1]:
        aux = x
        if (aux > v2):
            return "N"
        
        v2 = aux

    return "S" if  v1 <= v2 else "N"

n = int(input())
conj = []

for i in range(n):
    conj.append(list(map(int, input().split()))[1:])

if n >= 3 or n == 1:
    print("S")
else:
    print(isPossibleWithTwoConj(conj))