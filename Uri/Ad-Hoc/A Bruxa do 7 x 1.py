def mathSignal(s):
    if s == "x":
        return "*"
    
    return s

def notSeven(n):
    n = list(n)
    for x in range(len(n)):
        if n[x] == "7":
            n[x] = "0"
    
    return int(''.join(n))

a, s, b = map(str, input().split())
a = notSeven(a)
b = notSeven(b)
s = mathSignal(s)

result = str(eval(str(a)+s+str(b)))
print(int(notSeven(result)))


