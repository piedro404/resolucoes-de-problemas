import math

def isSumNumbersSquares(n):
    if(n>=0):
        for n1 in range(0, int(math.sqrt(n))+1):
            v = (n-(n1**2))
            if v >= 0:
                n2 = int(math.sqrt(v))  
                if ((n - ((n1**2)+(n2**2))) == 0):
                    return "YES"

    return "NO"

while True:
    try:
        x = int(input())
        print(isSumNumbersSquares(x))
    except EOFError:
        break
            