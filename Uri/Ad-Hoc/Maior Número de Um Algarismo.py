def sumAlgorismo(n):
    while len(n) > 1:
        n = str((sum(int(x) for x in n)))
    
    return int(n)

def maiorAlgorismo(x):
    n1 = sumAlgorismo(x[0])
    n2 = sumAlgorismo(x[1])
    if(n1 > n2):
        return 1
    elif(n1 < n2):
        return 2
    
    return 0

while True:
    try:
        x = input().split()
        if x[0] == x[1] == "0":
            break

        print(maiorAlgorismo(x))
    except EOFError:
        break