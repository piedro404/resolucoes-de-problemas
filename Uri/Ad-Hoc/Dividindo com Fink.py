def divFink(n):
    picaPau = 0
    fink = 0
    while (picaPau + fink) < n:
        picaPau +=1
        fink += picaPau
    
    return f"{fink} {(n-fink)}"

while True:
    x = int(input())
    if x == 0:
        break
    print(divFink(x))
