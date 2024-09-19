import math

while True:
    s = input().strip()
    
    if s == "0":
        break
    
    anagramas = math.factorial(len(s))
    
    print(anagramas)
