i = 1
while True:
    a, b = 0, 0
    x = int(input())
    if x==0:
        break
    print(f"Teste {i}")
    for _ in range(x):
        ar, br = map(int, input().split())
        a += ar
        b += br
        
    if a > b:
        print("Aldo")
    else:
        print("Beto")
        
    print()
    i+=1
        